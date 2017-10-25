# NoobPwn
The fourth of the pwn binaries, this one is a much easier pwnable binary

## Challenge Text
```
Getting tired of pwn? How about an easier one?

`nc pwn2.chal.gryphonctf.com 17346`

_Creator - @LFlare_
```

## Setup
1. Build both binaries with `cd generate && make`.
2. Build and run server docker image with `cd service && ./build.sh`.

## Solution
1. Apply the Euler's Algorithm to the binary.
2. Submit `0x31337` as decimal to read from `stdin`.
3. Enter in `GIMMEDAFLAG`.
4. Get flag.

<i>The creator did not published the full solutions for this challenge.</i>

### Flag
`GCTF{f1l3_d35cr1p70r5_4r3_n457y}`


