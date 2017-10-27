# ShellMethod
The second of the pwn binaries, this one is the classical buffer overflow problem in CTFs, with a twist, there isn't a `win()` function.

## Challenge Text
```
I've taken the previous challenge, tossed away the personality and replaced it with a stone cold robot AI.

`nc pwn2.chal.gryphonctf.com 17344`

_Creator - @LFlare_
```

## Setup
1. Build both binaries with `cd generate && make`.
2. Build and run server docker image with `cd service && ./build.sh`.

## Solution
**_Solutions in the `./solution` folder linked [HERE](./solution)_**

### Flag
`GCTF{5h3llc0d35_4r3_ju57_4553mbly}`

