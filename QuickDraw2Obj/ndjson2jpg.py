import os
import numpy as np
import tensorflow as tf
import json
import matplotlib.pyplot as plt

dataset = tf.data.TextLineDataset(['table.ndjson'])

for index, line in enumerate(dataset):
    if index % 1000 == 0:
        print(str(index) + ' of ~128000')
    jsonLine = json.loads(line.numpy())
    drawing = jsonLine['drawing']
    for stroke in drawing:
        plt.plot(stroke[0], [255 - y for y in stroke[1]], 'k')
        plt.axis('off')
    plt.savefig(os.path.join('images', str(index) + '.jpg'))

    with open(os.path.join('json', str(index) + '.json'), 'w') as file:
        file.write(json.dumps(drawing))

    plt.clf()
    # plt.show()

    if index == 5000:
        break
