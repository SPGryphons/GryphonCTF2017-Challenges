# Tsundeflow
The first of the pwn binaries, this one is the classical buffer overflow problem in CTFs. Beginner-friendly, to an extent!

## Challenge Text
```
This one is a handful.

Connect: `139.59.123.16 17343`

_Creator - @LFlare_
```

## Solution
**_More in-depth explanation at my writeups on [GitHub](https://github.com/LFlare/gryphonctf_2017_writeup)_**
1. Overwrite EIP to `win()`

## Setup
1. Build both binaries with `cd generate && make`.
2. Build server docker image with `cd service && ./build.sh`.
3. Run server docker image with `cd service && ./run.sh`.

## Flags
`GCTF{51mpl3_buff3r_0v3rfl0w_f0r_75und3r35}`
