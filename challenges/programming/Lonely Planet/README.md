# LonelyPlanet

## Question Text

WELCOME TO YOUR NEW JOB AT THE GALATIC FEDERATION AS A UNIVERSAL TRANSLATOR FOR OUR NEW CHAT APP "LONELYPLANET" DO YOUR JOB WELL!

Created by paux

## Setup Guide
1. run `bash start.sh`

## Distribution
text file with translations
- Translation.txt
text file describing translation.txt
- readme.txt

## Solution
1.	`nc 127.0.0.1 59949` will show that the program is running, however it has a timeout function so it would be almost impossible to complete the challenge by typing
2.	write a socket client program to interact with lonelyplanet
3.	split the received information and retrieve the origin language,origin text and wanted language
4.	using that, open the translation file and load it into a list 
5.	search for original word in list and return corresponding word in wanted language

## Recommended Reads

