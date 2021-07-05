from PIL import Image
import numpy as np
import tensorflow as tf
import os
import shutil
from tensorflow.python.data import AUTOTUNE

import hyperparameters as hp


def load_image(filepath):
    image = tf.io.read_file(filepath)
    image = tf.image.decode_jpeg(image, channels=1)
    return tf.image.convert_image_dtype(image, dtype=tf.float32)


def generate_kernel(horizontal=True):
    kernel_repeat = -np.ones((int(hp.kernel_size / 2)))
    kernel_repeat = np.append(kernel_repeat, [0])
    kernel_repeat = np.append(kernel_repeat, np.ones((int(hp.kernel_size / 2))))

    if horizontal:
        return np.transpose(np.full((hp.kernel_size, hp.kernel_size), kernel_repeat))
    else:
        return np.full((hp.kernel_size, hp.kernel_size), kernel_repeat)


def convolution(inp, kernel, output_filename):
    inp = tf.reshape(inp, (inp.shape[0], inp.shape[1]))
    outputs = np.empty((hp.num_convolutions + 1, inp.shape[0], inp.shape[1], 1))
    outputs[0] = np.copy(np.reshape(inp, (inp.shape[0], inp.shape[1], 1)))
    for i in range(0, hp.num_convolutions):
        output_width = int((inp.shape[1] - hp.kernel_size + 1 + 2 * hp.padding) / hp.stride)
        output_height = int((inp.shape[0] - hp.kernel_size + 1 + 2 * hp.padding) / hp.stride)
        output = np.zeros((output_height, output_width))

        print("Convolution " + str(i + 1) + " of " + str(hp.num_convolutions) + " (Output size: " + str(output_width) + "x" + str(output_height) + ")")

        for y in range(0, output_height):
            for x in range(0, output_width):
                output[y, x] = tf.reduce_sum(inp[y: y + hp.kernel_size, x: x + hp.kernel_size] * kernel).numpy()

        pad = int((outputs[0].shape[0] - output_height) / 2)
        if i % 10 == 0:
            output_tb = np.pad(output, pad, constant_values=1)
            outputs[int(i / 10) + 1] = np.reshape(output_tb, (output_tb.shape[0], output_tb.shape[1], 1))

            filename = output_filename + str(output_width) + 'x' + str(output_height)
            output_image = tf.reshape(output, (output.shape[0], output.shape[1], 1))
            with open(filename + str(i) + ".jpg", "wb") as fd:
                fd.write(tf.io.encode_jpeg(tf.image.convert_image_dtype(output_image, tf.uint8)).numpy())
        inp = output

    np.savetxt(filename + ".csv", output)

    return outputs


def log_images(images, index, label):
    file_writer = tf.summary.create_file_writer(logdir)
    with file_writer.as_default():
        tf.summary.image("Image (" + label + ")", images, step=index, max_outputs=10)


if __name__ == "__main__":
    logdir = "logs"
    if (os.path.isdir(logdir)):
        shutil.rmtree(logdir)

    train_dataset = tf.data.Dataset.list_files('train/images/*')

    train_dataset = train_dataset.map(load_image, num_parallel_calls=AUTOTUNE)
    # train_dataset = train_dataset.map(load_image)

    kernel_horz = generate_kernel()
    kernel_vert = generate_kernel(False)

    for index, image in enumerate(train_dataset):
        outputs_horz = convolution(image, kernel_horz, "horz" + str(index) + '_')
        log_images(outputs_horz, index, "horz")

        outputs_vert = convolution(image, kernel_vert, "vert" + str(index) + '_')
        log_images(outputs_vert, index, "vert")
