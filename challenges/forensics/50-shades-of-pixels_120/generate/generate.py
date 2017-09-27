#! /usr/bin/env python3
##
# Created for the 50 Shades of Pixels challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
from PIL import Image
from itertools import cycle
import os
import sys

# Set variables
MIN_SIZE = 128

# Get arguments
if len(sys.argv) == 2:
    flag = sys.argv[1]
else:
    quit()

# If flag too short, make it longer
if len(flag) < MIN_SIZE:
    flag = flag * int(MIN_SIZE / len(flag))

# Get width and height
width = len(flag) + 1
height = len(flag)

# Create image canvas
im = Image.new("RGB", (width, height))
pix = im.load()

# Build pixels
count = 0
for y in range(height):
    for x in range(width):
        asc = ord(flag[count % height])
        pix[x, y] = (asc, asc, asc)
        count += 1

# Save image
im.save("../distrib/flag.png", "PNG")
os.system("mv ../distrib/flag.png ../distrib/flag-`md5sum ../distrib/flag.png | cut -b-32`.png")

