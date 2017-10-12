# Turducken

## Question Text

We are having Turducken for dinner, but I only want chicken, can you get it for me?
Multiple tools have been used to prepare this dish though, you need to have java installed to attempt the challenge

Here are some recommended reads for you:
https://www.slideshare.net/hussainsavani/image-steganography
http://resources.infosecinstitute.com/steganography-and-tools-to-perform-steganography/
http://www.topbestalternatives.com/best-steganography-software/
https://www.geekdashboard.com/best-steganography-tools/

Enjoy~

Created by ESLunarPhoenix

## Distribution
Distribute all the contents inside `distrib` folder to the users

## Hints
* Check out the recommended reads
* The Pin is in the Title
* Analyse the task more
* Good luck~

## Solution
* The flag is embeded in an image in an image in an image
* Download OpenStego v0.7.1
* Download rSteg

Use the tools and passwords in the following order to get the flag
1. OpenStego:turkey
2. OpenStego:duck
3. rSteg:chicken

## Explaination

The flag is embeded in an image in an image in an image

This is similar to the idea of a turducken, which is a chicken in a duck in a turkey

The birds will also correspond to the passwords/key phrases used to hide the image

Upon downloading the file, you may notice there are two hashes in the filename. One is the md5 hash of the file. The other, can be cracked with a rainbow table online to retrive the original text: OpenStego

Alternatively, you can also view the hex values of the file, of which at the bottom, will have 'OpenStego0.7.1'

1. The first step is therefore using the OpenStego tool and the corresponding outerlayer of turducken, aka turkey to retrieve the embeded image
2. Repeating the first step with the 2nd layer will allow you to retrieve the last image to extract the flag from
3. The tool for the last step however, has not been directly provided in any way. You are meant to use the hint of the filename 'Don't forget the coffee' (an indirect reference to java) as well as the question text that multiple tools have been used and java is needed, in order to find the tool to retrieve the flag. Going through the recommended reads will allow you to find the other tools that use java and extract the flag

### Flag
`GCTF{H0n3st1y_I_pr3f3r_f1sh}`

## Recommended Reads
* https://www.slideshare.net/hussainsavani/image-steganography
* http://resources.infosecinstitute.com/steganography-and-tools-to-perform-steganography/
* http://www.topbestalternatives.com/best-steganography-software/
* https://www.geekdashboard.com/best-steganography-tools/
