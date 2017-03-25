#!/usr/bin/env python

import os

# A quick function to speak a string...
def speak(inString):
    inString = "espeak '" + inString + "'"
    os.system(inString)

def getTime(listOfKeys):
    # Need a general way of looking for keywords
    # Auto consideration of abbreviations, case in-sensitive
    # Basically a function which takes a list of common keys and generates
    # another list of derivatives from those. Use NLP/ anything
    if ('AM' or 'PM'or 'hrs'or 'hours') in listOfKeys:
        time_string = 1

if __name__ == '__main__':

    ip = input("Input command : ")
    listOfKeys = ip.strip().split()
    print(listOfKeys)


    pass


