# NoobPwn
The fourth of the pwn binaries, this one is a much easier pwnable binary

## Challenge Text
```
Getting tired of pwn? How about an easier one?

Connect: `139.59.123.16 17346`

_Creator - @LFlare_
```

## Solution
**_More in-depth explanation at my writeups on [GitHub](https://github.com/LFlare/gryphonctf_2017_writeup)_**
1. Apply the Euler's Algorithm to the binary.
2. Submit `0x31337` as decimal to read from `stdin`.
3. Enter in `GIMMEDAFLAG`.
4. Get flag.

## Setup
1. Build both binaries with `cd generate && make`.
2. Build server docker image with `cd service && ./build.sh`.
3. Run server docker image with `cd service && ./run.sh`.

## Flag
`GCTF{f1l3_d35cr1p70r5_4r3_n457y}`
