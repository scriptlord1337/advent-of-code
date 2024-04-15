# Day 1, part 1 of advent of code 2023
# This program looks for the first and last digit for every line in the input and then concatenates the two and finally calculates the sum of all lines.

import os, regex

# open the file and separate by lines into a list
dirname = os.path.dirname(__file__) #location of this file
filename = os.path.join(dirname, "input01.txt") #relative location of input file
my_file = open(filename, "r")
lines = my_file.readlines()

# initialize list of fetched numbers
numbers = []

# regex patterns
firstDigitPattern = regex.compile(r"^\D*(\d)")
lastDigitPattern = regex.compile(r"(\d)\D*$")

for line in lines:
    firstDigit = firstDigitPattern.search(line)
    lastDigit = lastDigitPattern.search(line)
    digitsconcat = (str(firstDigit.group(1)) + str(lastDigit.group(1)))
    numbers.append(int(digitsconcat))

print (sum(numbers))
