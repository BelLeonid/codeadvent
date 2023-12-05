import re

result = 0

file1 = open('text1.txt', 'r')
Lines = file1.readlines()

def func(input):
	if input == "one":
	    return "1"
	elif input == "two":
	    return "2"
	elif input == "three":
	    return "3"
	elif input == "four":
	    return "4"
	elif input == "five":
	    return "5"
	elif input == "six":
	    return "6"
	elif input == "seven":
	    return "7"
	elif input == "eight":
	    return "8"
	elif input == "nine":
		return "9"
	else: 
		return input
for line in Lines:
	# regex = re.findall('\d', line)
	# regex = re.findall('(?:\d|one|two|three|four|five|six|seven|eight|nine)', line, overlapped=True)
	regex = re.findall('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
	# r'(?=(\d{10}))'
	# print(regex)
	first = func(regex[0])
	last = func(regex[-1])
	result += int(first+last)
	# print(first, last)
print(result)