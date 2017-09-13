# Tsundeflow
As the simplest pwn challenge, this one is solvable by overflowing the address of `win()` to the `RET` address on the buffer. Calculating the amount of junk before reaching `RET` is as simple as `32` size of buffer + `4` address of the stack frame pointer, to reach `36`.

There is however, one more catch. The usage of `strlen` to check for buffer overflows, but wait! `strlen` counts characters in a `char[]`, and `char[]` ends with a `\x00` null byte, so we can trick the program into thinking we have lesser characters than there really is! So, we have to use `36` bytes of `\x00`.

Thus, by giving `36` bytes, we get to the `RET` address, which we will populate with `win()`'s address

Now, to find the address of `win()`, we can load it up in `gdb`,

    # gdb tsundeflow
    GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.04) 7.11.1
    Copyright (C) 2016 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
    and "show warranty" for details.
    This GDB was configured as "x86_64-linux-gnu".
    Type "show configuration" for configuration details.
    For bug reporting instructions, please see:
    <http://www.gnu.org/software/gdb/bugs/>.
    Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.
    For help, type "help".
    Type "apropos word" to search for commands related to "word"...
    gdb> p &win
    $1 = (<text variable, no debug info> *) 0x80484eb <win>

Bingo! Now all we have to do is code it little-endian and submit it as our payload with the junk data. `0x80484eb` becomes `\xeb\x84\x04\x08`.

Another way of getting the address involves [pwntools](https://github.com/Gallopsled/pwntools), which is represented in the [solutions](solve.py).
