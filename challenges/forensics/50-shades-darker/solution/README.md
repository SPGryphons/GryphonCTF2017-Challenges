# 50 Shades Darker
Solution to this challenge can be done in many ways, though my personal recommendation is through Python's `PIL` library. Additionally, this challenge is built off the previous challenge, 50 Shades Brighter.

With the only clue word, "darker", participants are expected to think logically and play with brightness settings on the image, except the correct answer, unlike the previous challenge is to bitshift **rotate** it.

An example of bitshift rotating, or circular bitshifting, is as follows,

    b1001 >> 1 = b1100
    b1100 << 2 = b0011

It is however, important to note that colour values are inherently limited to `255`, or `8` bits, so bit masking using `&` must also be done to prevent overflowing or underflowing.

All of the above is also easily accomplished in [Python](solve.py) and using the Pillow library.
