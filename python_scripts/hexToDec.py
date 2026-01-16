#!/usr/bin/env python
import sys

reverseInput = sys.argv[1][::-1]

digitConvert = { '0':0 , '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }

exponent , decimal number = 0 , 0
for character in reverseInput:
    decimalNumber = decimalNumber + (digitConvert[character] * (16 ** exponent))
    exponent = exponent + 1

print(decimalNumber)