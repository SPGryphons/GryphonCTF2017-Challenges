# Internal

## Question Text

Yet to be decided

Created by void & exetr

## Setup Guide
1. Create a new vm and add vmdk as disk to vm

## Distribution

## Solution
1. Use the ALFA cards provided and hack the wifi
2. Upon accessing the network, a nmap scan for active ports will show a server running a service on port 80
3. null bye inject -> passwd & users
4. From the information gathered, we know that there is a ssh service that allows sftp to users
5. With the staff list, you are able to run a bruteforce attack
6. Using metasploit, the password can easily be guessed to be `A1H3LL01`
7. With all this information, you will be able to get the file from the user home directory using sftp.
8. Opening up the files, you will see that there is a file that contains some text
9. Upon decoding using Base64, you will get the flag.

## Recommended Reads

## Flag
`GCTF{wir3l355_i5_s0_much_>_th4n_3th3rn37}`
