# 50 Shades of Pixels
Solution to this challenge can be done in many ways, though my personal recommendation is through Python's `PIL` library.

Initially, receiving the file might give some people headaches wondering how I hid the message. Well, the very interesting pattern of shades of grey pixels might give you a hint. The message is encoded in the red, blue and green values of the pixels.

Reading the pixels from top left to top right will grant you the message, it's really easily solved in [Python](solve.py). You might need to install `pip` and run `pip install pillow` to get the neccessary libraries for this to work.
