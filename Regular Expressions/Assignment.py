#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
fname = input("Enter the filename:")
if len(fname) == 0:
    fname = "regex_sum_42.txt"

try:
    fh = open(fname)
except:
    print("File does not exist")
    quit()

total = 0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for number in numbers:
            total = total + int(number)

print(total)
