# RNG

## Question Text
I've harnessed the power of C to make a random number generator. Although, I feel i might have left the flag somewhere inside the program...

*Creator - Chuan Kai (@exetr)*

## Setup Guide
1. Compile rng.c with `cc -o rng rng.c`

## Distribution
1. Distribute the executable in distrib folder

## Solution 
1. Using the strings command in linux, the flag can be revealed within the binary `strings rng`
### Flag
`GCTF{i_th1nk_i_m4y_h4v3_f0rg077en_th15}`