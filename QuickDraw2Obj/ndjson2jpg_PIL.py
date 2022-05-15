import os
from functools import reduce
import tensorflow as tf
import json
from PIL import Image, ImageDraw

MAX_JPGS = 5000

dataset = tf.data.TextLineDataset(['../full_simplified_car.ndjson'])

for index, line in enumerate(dataset):
    if index % 1000 == 0:
        print(f'{index} of {MAX_JPGS}')
    jsonLine = json.loads(line.numpy())
    drawing = jsonLine['drawing']

    im = Image.new('RGB', (256, 256), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    # normalise coords to center the drawing
    x_coords = reduce(lambda a, b: a + b, [stroke[0] for stroke in drawing])
    displacement_x = int((256 - min(x_coords) - max(x_coords)) / 2)
    y_coords = reduce(lambda a, b: a + b, [stroke[1] for stroke in drawing])
    displacement_y = int((256 - min(y_coords) - max(y_coords)) / 2)

    for stroke in drawing:
        draw.line(list(zip([x + displacement_x for x in stroke[0]], [y + displacement_y for y in stroke[1]])), fill=0)

    im.save(os.path.join('cars', str(index) + '.jpg'), 'JPEG')

    with open(os.path.join('json', str(index) + '.json'), 'w') as file:
        file.write(json.dumps(drawing))

    if index == 5000:
        break
