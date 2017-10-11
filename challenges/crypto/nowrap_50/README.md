# NoWrap
This is an intermediate RSA challenge, where the flaw is simply a message too short and an exponent too small to cause the modulus from taking effect.

## Challenge Text
```
My white candy wrapper had this weird numbers encoded in it's molecular structure, I think it might contain the full recipe of the candy, can you help me get to the bottom of it?

Creator: Amos (LFlare) Ng
```

## Solution
**_More in-depth explanation at my writeups on [GitHub](https://github.com/LFlare/gryphonctf_2017_writeup)_**
1. `e` too small for modulo `N` to hide message.
2. `e`-root.

## Flag
`GCTF{7h3_m355463_15_h1l4r10u5ly_5h0r7}`
