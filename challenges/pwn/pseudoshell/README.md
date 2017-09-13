# ShellMethod
The third of the pwn binaries, this one is a overflow challenge taken into the opposite end, with the focus on domino effects.

## Challenge Text
```
I managed to hook on to a shady agency's server, can you help me secure it?

Connect @ 188.166.248.233:9994

Created By: Amos (LFlare) Ng
```

## Setup
1. Build both binaries with `cd generate && make`.
2. Build server docker image with `cd service && ./build.sh`.
3. Run server docker image with `cd service && ./run.sh`.
