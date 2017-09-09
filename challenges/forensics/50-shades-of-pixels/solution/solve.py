#! /usr/bin/env python3
##
# Created for the 50 Shades of Pixels challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
from PIL import Image
from itertools import cycle
import sys

# Open file
im = Image.open("../distrib/flag.png")
pix = im.load()
width, height = im.size

# Read flag from file
flag = []
for x in range(width):
    r, g, b = pix[x, 0]
    char = chr(r)
    flag.append(char)

    # Check if closing bracket, just asthetics
    if char == "}":
        break

# Output repeated flags
print("".join(flag))
