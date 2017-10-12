# 50 Shades Darker
This has no references to any films, characters, bibliographies or books. This is just pure jest of a parody challenge. As the third step in pixel steganography, this challenge encourages logical thinking towards the challenge name but also flexible thinking when conventional methods no longer work.

## Challenge Text
```
Alice - "Wow, I know I said it was too dark earlier but this is way too bright!"
Bob - "Are you serious!? Fine! Whatever suits you!"
Alice - "..."
Bob - "..."
Alice - "This seems weird."

Creator: Amos (LFlare) Ng
```

## Solution
Solution to this challenge can be done in many ways, though my personal recommendation is through Python's `PIL` library. Additionally, this challenge is built off the previous challenge, 50 Shades Brighter.

With the only clue word, "darker", participants are expected to think logically and play with brightness settings on the image, except the correct answer, unlike the previous challenge is to bitshift **rotate** it.

An example of bitshift rotating, or circular bitshifting, is as follows,

    b1001 >> 1 = b1100
    b1100 << 2 = b0011

It is however, important to note that colour values are inherently limited to `255`, or `8` bits, so bit masking using `&` must also be done to prevent overflowing or underflowing.

All of the above is also easily accomplished in [Python](solution/solve.py) and using the Pillow library.

### Flag
`GCTF{7h15_d4rkn355_15_n07_45_3xp3c73d_3h}`
