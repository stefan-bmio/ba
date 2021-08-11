import os

input_path = 'train/classes/*'
result_path = "results"
images_path = os.path.join(result_path, "images")
filenames_file = "filenames.csv"
label_horizontal = "horiz"
label_vertical = "vert"
save_last_intermediates = 2
