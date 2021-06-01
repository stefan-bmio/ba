import cv2 as cv
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="path to image")
parser.add_argument("--output", required=True, help="path to output image")
args = parser.parse_args()

img = cv.imread(args.input, cv.IMREAD_GRAYSCALE)
edges = cv.Canny(img, 100, 200)
edges = (255 - edges)
# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()
cv.imwrite(args.output, edges)

# import os
# import cv2 as cv
# for filename in os.listdir('tables'):
#     cv.imwrite(os.path.join('edges', filename), 255 - cv.Canny(cv.imread(os.path.join('tables', filename)), 100, 200))