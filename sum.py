# Sums the numbers found in a file. Searches using Regular Expressions.
import re

handle = open('regex_sum_1971294.txt')
#handle = open('regex_sum_42.txt')
#Try sample to test output of program
#handle = open('try.txt')
numlist = list()
#mysum = 0

# For loop to loop through the file 
for line in handle:
    # Get rid of white space
    line = line.rstrip()
# Extract all numbers 
    textnum = re.findall('([0-9]+)', line)
    if len(textnum) < 1: continue
    # Append numbers to the list.
    for numb in range(len(textnum)):
       num = int(textnum[numb])
       numlist.append(num)

#Print out the list to make sure it isn't skipping any lines.
#print(numlist)

# Print the sum of integers found in the file.
print(sum(numlist))
