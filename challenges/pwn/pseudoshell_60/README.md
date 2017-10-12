# PseudoShell
The third of the pwn binaries, this one is a overflow challenge taken into the opposite end, with the focus on domino effects.

## Challenge Text
```
I managed to hook on to a shady agency's server, can you help me secure it?

`nc pwn2.chal.gryphonctf.com 17341`

_Creator - @LFlare_
```

## Solution
1. Simple buffer overflow to overwrite `access`.
2. Get flag.

<i>The creator did not published the full solutions for this challenge.</i>

### Flag
`GCTF{0ff_by_0n3_r34lly_5uck5}`

## Setup
1. Build both binaries with `cd generate && make`.
2. Build server docker image with `cd service && ./build.sh`.
3. Run server docker image with `cd service && ./run.sh`.

