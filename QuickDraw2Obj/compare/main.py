import os
import glob
import numpy as np
import tensorflow as tf
import re

import constants


if __name__ == "__main__":
    input0 = []
    input1 = []
    index_to_filename0 = {}
    index_to_filename1 = {}
    for filename in glob.glob(os.path.join(constants.input_path0, constants.horizontal_glob)):
        input0.append(np.loadtxt(filename))
        index_to_filename0[int(re.match(".*horiz(\\d+).*", filename).groups()[0])] = filename

    for i, filename in enumerate(glob.glob(os.path.join(constants.input_path1, constants.horizontal_glob))):
        input1.append(np.loadtxt(filename))
        index_to_filename1[int(re.match(".*horiz(\\d+).*", filename).groups()[0])] = filename

    differences = []
    for i0, in0 in enumerate(input0):
        differences.append([])
        for i1, in1 in enumerate(input1):
            differences[i0].append([])
            differences[i0][i1].append(tf.reduce_sum(tf.abs(tf.subtract(in0, in1))))

    result = []
    for diff in differences:
        result.append(tf.argmin(diff))

    original_filenames0 = np.loadtxt(constants.filenames0_file, dtype=np.str)
    original_filenames1 = np.loadtxt(constants.filenames1_file, dtype=np.str)

    for i, similar in enumerate(result):
        print(str(i) + ": " + index_to_filename0[i] + " -> " + index_to_filename1[similar.numpy()[0]])
        print("(" + original_filenames0[i] + " -> " + original_filenames1[similar.numpy()[0]] + ")")
