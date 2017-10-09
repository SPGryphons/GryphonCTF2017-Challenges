# Internal

## Question Text

Yet to be decided

### Hint 1
`\0`

Created by void & exetr

## Setup Guide
1. Create a new vm and add vmdk as disk to vm
`User: root`
`Password: thisisasecurepassword`

## Distribution

## Solution Part 2
1.  Use the ALFA cards provided and hack the wifi
2.  Upon accessing the network, a nmap scan for active ports will show a server running a service on port 80
3.  Presented with a login screen, use simple SQL Injection codes such as `'OR 1=1 --` to get access
4.  Presented with a rather empty site, there is a hyperlink for suppoused terms and conditions which leads to `ftp.php?file=tnc.txt`
5.  Removing the `file` variable, a directory listing of `/ftp` is presented and we can see some juicy files
6.  Trying to access any files that do not end with `.txt` brings up an error
7.  To bypass this, use null byte injection to overcome the check and access the files you want
8.  From the information gathered, we know that there is a ssh service that allows sftp to users
9.  With the staff list, you are able to run a bruteforce attack
10. Using metasploit, the password can easily be guessed to be `A1H3LL01`
11. With all this information, you will be able to get the file from the user home directory using sftp.
12. Opening up the files, you will see that there is a file that contains some text
13. Upon decoding using Base64, you will get the flag.

## Recommended Reads

## Flag
`GCTF{wir3l355_i5_s0_much_>_th4n_3th3rn37}`
