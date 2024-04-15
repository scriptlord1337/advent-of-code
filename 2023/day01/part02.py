# Day 1, part 1 of advent of code 2023
# This program looks for the first and last numeric or written english digit for every line in the input and then concatenates the two, and finally calculates the sum of all lines.

import os, regex

# open the file and separate by lines into a list
dirname = os.path.dirname(__file__) #location of this file
filename = os.path.join(dirname, "input01.txt") #relative location of input file
my_file = open(filename, "r")
lines = my_file.readlines()

def alphabeticToNumeric(inputnumber):
    wordList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if inputnumber in wordList:
        return wordList.index(inputnumber)
    else:
        return inputnumber

# initialize list of fetched numbers
numbers = []

# regex patterns
digitPattern = regex.compile(r"\d|zero|one|two|three|four|five|six|seven|eight|nine", regex.IGNORECASE)

for line in lines:
    digits = digitPattern.findall(str(line), overlapped=True) #overlapped is very important to catch cases like "twone"

    firstDigit = alphabeticToNumeric(digits[0].lower())
    lastDigit = alphabeticToNumeric(digits[-1].lower())
    
    digitsconcat = (str(firstDigit) + str(lastDigit))
    numbers.append(int(digitsconcat))

print (sum(numbers))
