# 50 Shades of Pixels
This has no references to any films, characters, bibliographies or books. This is just pure jest of a parody challenge. As the first step in pixel steganography, I think this challenge will introduce players to scripting as a way of solving challenges.

## Challenge Text
```
Bob - "I don't do plaintext."
Bob - "My methods of communication are unconventional."
Alice - "So show me?"
Bob - "Okay!"

Creator: Amos (LFlare) Ng
```

## Hints
```
Perhaps the colours mean something?
```

## Solution
**_More in-depth explanation at my writeups on [GitHub](https://github.com/LFlare/gryphonctf_2017_writeup)_**
1. Starting from top-left corner, retrieve pixel colour values.
2. Shift values circular left by 1.
3. Convert colour values to ASCII character.
4. Rinse and repeat till you get the flag.

## Flag
`GCTF{p1x3l1z3d_53cr375_4r3_h4w7}`
