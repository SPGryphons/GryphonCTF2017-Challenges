# Internal

## Question Text

I heard that the organisers are storing a flag in their internal network. Looks like there's wifi???

Creators - @void, @exetr & @zxlim

## Setup Guide
1.  Run the script in service/Internal-01 on a new install of a Debian-based vm.

## Distribution

## Solution
1.  Use the ALFA cards provided and hack the wifi
2.  Upon accessing the network, a nmap scan for active ports will show a server running a service on port 80
3.  Presented with a login screen, use simple SQL Injection codes such as `'OR 1=1 --` to get access
4.  Presented with a rather empty site, there is a hyperlink for suppoused terms and conditions which leads to `ftp.php?file=tnc.txt`
5.  Removing the `file` variable, a directory listing of `/ftp` is presented and we can see some juicy files
6.  3 files of interest are users, welcome.info and password.bck
7.  However, trying to access these files brings up an error since they do not end with `.txt`
8.  To bypass this, use null byte injection to overcome the check and access the files
8.  From the information gathered, we know that there is a ssh service that allows sftp to users
9.  With the users list, you are able to run a bruteforce attack
10. Using metasploit, the password can easily be guessed to be `A1H3LL01`
11. You will then be able to get the file from the user home directory using sftp.
12. Opening up the files, you will see that there is a file that contains some text that seems to be encoded in Base64
13. You can get the flag easily using any online base64 decoder

## Recommended Reads

## Flag
`GCTF{wir3l355_i5_s0_much_>_th4n_3th3rn37}`
