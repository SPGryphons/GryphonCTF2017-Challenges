# My nice site
Curl doesn't run Javascript

<i>Creator - @Platy</i>

## Question
>Void has been working hard during the holidays. He says he has a very nice website that he coded. However, I cannot seem to open it. Can you help me?

http://web.chal.gryphonctf.com:17566

## Setup Guide
Do `sudo bash build.sh`

## Distribution
None.

## Solution
There is Javascript running a script that will crash the browser. Since curl doesn't load Javascript, we can use that

Do `curl web.chal.gryphonctf.com:17566` to get the flag

### Flag
`GCTF{j4v45cr1p7_15_d4n63r0u5}`

## Credits
void for coming up with the idea
