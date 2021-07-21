import tensorflow as tf
import json
import matplotlib.pyplot as plt
import os

dataset = tf.data.TextLineDataset(['table.ndjson'])

for index, line in enumerate(dataset):
    if index < 27658:
        continue
    jsonLine = json.loads(line.numpy())
    drawing = jsonLine['drawing']
    for stroke in drawing:
        plt.plot(stroke[0], [255 - y for y in stroke[1]], 'k')
        plt.axis('off')
    plt.savefig(os.path.join('images', str(index) + '.jpg'))
    plt.clf()
    # plt.show()
