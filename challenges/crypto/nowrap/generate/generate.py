#! /usr/bin/env python3
##
# Created for the NoWrap challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
import sys
from base64 import b16encode
from Crypto.PublicKey import RSA

# Generate a key for us to use!
key = RSA.generate(4096, e=3)

# Prepare our flag
if len(sys.argv) != 2:
    quit()
flag = "Our secret flag has to be: " + sys.argv[1]
m = int(b16encode(flag.encode()), 16)
c = pow(m, key.e, key.n)

# Output our now 'safe' flag!
with open("../distrib/flag.txt", "w") as file:
    file.write("n = {0}\ne = {1}\nc = {2}\n".format(key.n, key.e, c))
