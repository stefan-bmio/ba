import os
import math
import numpy as np
import tensorflow as tf
import os
import shutil
from tensorflow.python.data import AUTOTUNE

import constants
import hyperparameters as hp


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
        output_height = int((inp.shape[0] - hp.kernel_size + 1 + 2 * hp.padding) / hp.stride)
        output_width = int((inp.shape[1] - hp.kernel_size + 1 + 2 * hp.padding) / hp.stride)
        output = np.zeros((output_height, output_width))

        print("Convolution " + str(i + 1) + " of " + str(hp.num_convolutions) + " (Output size: " + str(output_width) + "x" + str(output_height) + ")")

        for y in range(0, output_height):
            img_y = y * hp.stride
            for x in range(0, output_width):
                img_x = x * hp.stride
                output[y, x] = tf.reduce_sum(tf.math.multiply(
                    inp[img_y: img_y + hp.kernel_size, img_x: img_x + hp.kernel_size], kernel)
                ).numpy()

        pad_y = (outputs[0].shape[0] - output_height) / 2
        pad_x = (outputs[0].shape[1] - output_width) / 2

        output_tb = np.pad(output, ((math.floor(pad_y), math.ceil(pad_y)), (math.floor(pad_x), math.ceil(pad_x))), constant_values=1)
        outputs[i + 1] = np.reshape(output_tb, (output_tb.shape[0], output_tb.shape[1], 1))

        filename = output_filename + str(output_width) + 'x' + str(output_height)
        output_image = tf.reshape(output, (output.shape[0], output.shape[1], 1))
        with open(os.path.join(constants.images_path, filename + "_" + str(i) + ".jpg"), "wb") as fd:
            fd.write(tf.io.encode_jpeg(tf.image.convert_image_dtype(output_image, tf.uint8)).numpy())

        if i >= hp.num_convolutions - constants.save_last_intermediates:
            np.savetxt(os.path.join(
                constants.result_path, filename + "_" + ".csv"), output)

        inp = output


    return outputs


def log_images(images, index, label):
    file_writer = tf.summary.create_file_writer(logdir)
    with file_writer.as_default():
        tf.summary.image("Image (" + label + ")", images, step=index, max_outputs=hp.num_convolutions + 1)


if __name__ == "__main__":
    logdir = "logs"
    if (os.path.isdir(logdir)):
        shutil.rmtree(logdir)

    train_dataset = tf.data.Dataset.list_files(constants.input_path)

    filenames = []
    kernel_horz = generate_kernel()
    kernel_vert = generate_kernel(False)

    for index, filepath in enumerate(train_dataset):
        print("processing image " + str(index + 1))
        filenames.append(filepath.numpy())
        image = tf.io.read_file(filepath)
        image = tf.image.decode_jpeg(image, channels=1)
        image = tf.image.convert_image_dtype(image, dtype=tf.float32)

        outputs_horz = convolution(image, kernel_horz, constants.label_horizontal + str(index) + '_')
        log_images(outputs_horz, index, constants.label_horizontal)

        outputs_vert = convolution(image, kernel_vert, constants.label_vertical + str(index) + '_')
        log_images(outputs_vert, index, constants.label_vertical)

    np.savetxt(constants.filenames_file, [filename.decode() for filename in filenames], fmt="%s")
