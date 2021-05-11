#!/usr/bin/python3

import os
from PIL import Image

# This file will iterate over a series of images
# scaling them down, rotating them by 90 degrees
# and then converting them to a different format

src_dir = "/home/student-00-de2bf90de6eb/images" #The file path for the source directory
prt_dir = "/home/student-00-de2bf90de6eb/opt/icons" #The file path for the output directory

for filename in os.listdir(src_dir):
    src_path = src_dir + "/" + filename
    if src_path[-4:] == "48dp":
        prt_path = prt_dir + "/" + filename
        im = Image.open(src_path)
        im = im.resize((128,128))
        im = im.rotate(270)
        im = im.convert("RGB")
        im.save(prt_path,"JPEG")