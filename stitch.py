from PIL import Image
import numpy as np
import cv2

# TODO: PIL can do image stitching, no need to bother with np arrays


def join_vertically(dir_path, files):
    files_arr = read_files(dir_path, files)
    final_image = np.concatenate(files_arr)
    return final_image


def join_horizontally(parts):
    par = np.concatenate(parts, axis=1)
    return Image.fromarray(par)


def read_files(path, files):
    files_array = []
    for i in files:
        img = cv2.cvtColor(cv2.imread(path + i), cv2.COLOR_BGR2RGB)
        files_array.append(img)
    return files_array


def __find_shape(path, files):
    rows, columns = 0
    files_arr = read_files(path, files)
    for img in files_arr:
        rows += img.shape[0]
        if int(img.shape[1]) > columns:
            columns = img.shape[1]
    return (rows, columns)


def save_img(image, name):
    image.save(name + ".png")
