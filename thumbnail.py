import os
import cv2
import re
import shutil

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

for i in range(1,60):
    path = f"./work/{i}"
    file_list = os.listdir(path)
    firstImage = [file for file in file_list if file.startswith("1.")]
    print(f"{path}/{firstImage[0]}")
    originImage = cv2.imread(f"{path}/{firstImage[0]}", cv2.IMREAD_UNCHANGED)
    resizedImage = image_resize(originImage, height = 600)
    cv2.imwrite(f"thumbnail{i}.png", resizedImage)