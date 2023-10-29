import re

hand = input("Enter the file: ")
fhand = open(hand).read()

integers = re.findall('[0-9]+',fhand)


sum = 0

for number in integers:
    num = int(number)
    sum = sum + num

print(sum)