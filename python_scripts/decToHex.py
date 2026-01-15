#!/usr/bin/env python
import sys

inputNumber = sys.argv[1]

if not inputNumber.isnumeric():
    print("Input not numeric!")
    sys.exit()

quo = 0
rem = 0
digits = []

number = int(inputNumber) 

while True:
    quo = number // 16
    rem = number % 16
    digits.append(rem)

    if quo == 0:
        break
    else:
        number = quo

digitConvert= ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

hexString = ""
for digit in digits:
    hexString = digitConvert[digit] + hexString

if len(hexString) % 2 != 0:
    hexString = "0" + hexString

print(hexString)