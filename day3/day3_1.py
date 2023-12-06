import re

result = 0

file1 = open('text1.txt', 'r')
Lines = file1.readlines()

result = 0

class Number:
  def __init__(self, line, value, start, end):
    self.line = line
    self.value = value
    self.start = start
    self.end = end
    self.length = len(str(value))

linecounter = 0
numbers = []
for line in Lines:
	regex = re.finditer('\d+', line)
	for match in regex:
		newNumber = Number(linecounter, match[0], match.start(), match.end())
		numbers.append(newNumber)
	linecounter += 1 

for number in numbers:
	linesToCheck = [Lines[number.line]]
	isActual = False
	if number.line != 0 :
		linesToCheck.append(Lines[number.line - 1])
	if number.line != len(Lines) - 1:
		linesToCheck.append(Lines[number.line + 1])

	for line in linesToCheck:
		cutLine = line[max(0, number.start - 1):min(number.end + 1, len(line) - 1)]
		cutLine = cutLine.replace(".", "")
		cutLine = ''.join(filter(lambda z: not z.isdigit(), cutLine))
		if len(cutLine) > 0:
			isActual = True
			result += eval(number.value)
			# print("Number " + number.value + " is good!")
			break
	# print("Number " + number.value + " is bad!")

print(result)