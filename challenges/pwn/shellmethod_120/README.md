# ShellMethod
The second of the pwn binaries, this one is the classical buffer overflow problem in CTFs, with a twist, there isn't a `win()` function.

## Challenge Text
```
I've taken the previous challenge, tossed away the personality and replaced it with a stone cold robot AI.

`nc pwn2.chal.gryphonctf.com 17344`

_Creator - @LFlare_
```

## Solution
Slightly more challenging than Tsundeflow, this one requires the knowledge of shellcodes. Shellcodes are essentially machine language, compiled in the form to execute a shell, commonly `/bin/sh`. Additionally, the binary is built to be easier for juniors by enabling execution on heap/stack. For this solution, we will be going with a very classical approach to things.

### Preparation
Before we can get started, we have to know what we need.

1. Shellcode
2. Address of buffer

Firstly, shellcode. This can be easily obtained pre-compiled at [shell-storm](https://shell-storm.org/shellcode). We want to be targetting `Linux/x86` as that is our predetermined challenge architecture. For my solution, I took the shellcode, `\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80`.

Secondly, address of buffer. This one is slightly harder to get if you are new to GDB. Generally, the process is simple. When entering into the `command` variable, enter a string like `AAAABBBBCCCCDDDD`, then search through program runtime memory for that specific string. For this particular challenge, we want to isolate the address on the heap, starting with `0x804`.

## Pwn Time
Now we can get down to crafting our payload. Essentially, we want the program to execute what we type in, so like the previous, we can hijack the `ret` address to point towards our own buffer. As the `command` variable is `64` bytes long, we can conclude that the `ret` address is `64 + 4` bytes offsetted, so we will need to form our payload like so,

    [SHELLCODE - x bytes][JUNK - (68 - x) bytes][ADDRESS OF BUFFER]

However, I like to spice things up a little by using a little bit of `NOP`sledding.

    [NOP - (64 - x) bytes][SHELLCODE - x bytes][JUNK - 4 bytes][ADDRESS OF BUFFER]

This allows for a little bit more flexibility with buffer addressing, as the compiler will ignore the NOP bytes and continue on down towards our shellcode.

Like the previous challenge, this is simplified in [python](solution/solve.py).

### Flag
`GCTF{5h3llc0d35_4r3_ju57_4553mbly}`

## Setup
1. Build both binaries with `cd generate && make`.
2. Build server docker image with `cd service && ./build.sh`.
3. Run server docker image with `cd service && ./run.sh`.

