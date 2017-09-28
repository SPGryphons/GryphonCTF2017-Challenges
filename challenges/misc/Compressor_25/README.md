# Compressor

## Question Text
I want to make my text file very very small! So, I did what any sane person would do and shoved it into my compressor and ran it 10 times!

## Setup Guide
1. Convert flag.txt to binary
2. Convert binary.txt to base64.txt
3. `cp base64.txt level10`
4. `genisoimage -o level9 level10`
5. `lzop -k level9 -o level8`
6. `rzip -k level8 -o level7`
7. `xz -k -c -z level7 > level6`
8. `lzip -c -k level6 > level5`
9. `bzip2 -z -k -c level5 > level4
10. `tar -cvf level3 level4`
11. `gzip -k -c level3 > level2`
12. `zip level1 level2`
13. `rar a level0 level1`

## Distribution
1. Distribute the file in distrib folder

## Solution 
1. `rar x level0.rar`
2. `unzip level1`
3. Rename level2 to level2.gz with `mv level2 level2.gz`
4. `gzip -d -k -c level2.gz > level3`
5. `tar -xvf level3 level4`
6. `bzip2 -d -k -c level4 > level5`
7. `lzip -d -c -k level5 > level6`
8. `xz -d -k -c level6 > level7`
9. `rzip -k -d level7 -o level8`
10. `lzop -k -d level8 -o level9`
11. Make a temp directory `mkdir /temp` and mount it using `mount level9 /temp`
12. Run `cat level10` to see the contents
13. Decode from base64 and then from binary to get the flag

### Flag
`GCTF{i_th1nk_i_m4y_h4v3_f0rg077en_th15}`