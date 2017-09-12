# I Need Moar!

## Question Text
There is this upcominng football match.

I want to buy 100 tickets so that i can resell them on carousell to make a profit :D

However, the site does not let me book more than 5 tickets.
 
I wonder how I can all 100 at once...

*Creator - Chuan Kai (@exetr)*

## Setup Guide
1. 

## Solution
1. Using a software with proxy interception capability, such as Burp Suite, intercept the HTTP POST request
2. Modify the value of `quantity` to `100`
3. Forward the request to get the flag
### Flag
`GCTF{T1m3_t0_up53ll_on_c4r0us311_h3h3h3}`