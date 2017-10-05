# ShellMethod
The second of the pwn binaries, this one is the classical buffer overflow problem in CTFs, with a twist, there isn't a `win()` function.

## Challenge Text
```
I've taken the previous challenge, tossed away the personality and replaced it with a stone cold robot AI.

Connect: `139.59.123.16 17344`

_Creator - @LFlare_
```

## Setup
1. Build both binaries with `cd generate && make`.
2. Build server docker image with `cd service && ./build.sh`.
3. Run server docker image with `cd service && ./run.sh`.

## Flag
`GCTF{5h3llc0d35_4r3_ju57_4553mbly}`
