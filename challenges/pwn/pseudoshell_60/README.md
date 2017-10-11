# PseudoShell
The third of the pwn binaries, this one is a overflow challenge taken into the opposite end, with the focus on domino effects.

## Challenge Text
```
I managed to hook on to a shady agency's server, can you help me secure it?

Connect: `139.59.123.16 17341`

_Creator - @LFlare_
```

## Solution
**_More in-depth explanation at my writeups on [GitHub](https://github.com/LFlare/gryphonctf_2017_writeup)_**
1. Simple buffer overflow to overwrite `access`.
2. Get flag.

## Setup
1. Build both binaries with `cd generate && make`.
2. Build server docker image with `cd service && ./build.sh`.
3. Run server docker image with `cd service && ./run.sh`.

## Flag
`GCTF{0ff_by_0n3_r34lly_5uck5}`
