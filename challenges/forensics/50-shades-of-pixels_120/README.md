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
Solution to this challenge can be done in many ways, though my personal recommendation is through Python's `PIL` library.

Initially, receiving the file might give some people headaches wondering how I hid the message. Well, the very interesting pattern of shades of grey pixels might give you a hint. The message is encoded in the red, blue and green values of the pixels.

Reading the pixels from top left to top right will grant you the message, it's really easily solved in [Python](solution/solve.py). You might need to install `pip` and run `pip install pillow` to get the neccessary libraries for this to work.

### Flag
`GCTF{p1x3l1z3d_53cr375_4r3_h4w7}`
