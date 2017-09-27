#! /usr/bin/env python3
##
# Created for the Insanity challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
import os
import sys
import random
from base64 import *

# Variables
DIFFICULTY = 5
ENCODERS = [b16encode, b32encode, b64encode]

# Ensure flag given
if len(sys.argv) != 2:
    quit()

# Repeatedly encode flag
flag = sys.argv[1].encode()
for i in range(DIFFICULTY):
    flag = random.choice(ENCODERS)(flag)

# Save flag to file
with open("../distrib/flag.txt", "w") as file:
    file.write(flag.decode())

# Update hash
os.system("mv ../distrib/flag.txt ../distrib/flag-`md5sum ../distrib/flag.txt | cut -b-32`.txt")
