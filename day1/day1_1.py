import re

result = 0

file1 = open('text1.txt', 'r')
Lines = file1.readlines()

for line in Lines:
	regex = re.findall('\d', line)
	first = regex[0]
	last = regex[-1]
	result += int(first+last)
	# print(first, last)
print(result)