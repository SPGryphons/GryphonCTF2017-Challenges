# PseudoShell
The third of the pwn binaries, this one is a overflow challenge taken into the opposite end, with the focus on domino effects.

## Challenge Text
```
I managed to hook on to a shady agency's server, can you help me secure it?

`nc pwn2.chal.gryphonctf.com 17341`

_Creator - @LFlare_
```

## Setup
1. Build both binaries with `cd generate && make`.
2. Build and runserver docker image with `cd service && ./build.sh`.

## Solution
**_Solutions in the `./solution` folder linked [HERE](./solution)_**

### Flag
`GCTF{0ff_by_0n3_r34lly_5uck5}`


