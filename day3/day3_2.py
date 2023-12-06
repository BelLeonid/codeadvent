import re

result = 0

file1 = open('text1.txt', 'r')
Lines = file1.readlines()

result = 0

def checkNumberAppropriateLine(number, lineNumber):
	if (number.line >= lineNumber-1 and number.line <= lineNumber+1):
		return True
	else:
		return False

def checkNumberAppropriatePosition(number, gearPosition):
	if ((number.end >= gearPosition and number.end <= gearPosition+2) or (number.start >= gearPosition-1 and number.start <= gearPosition+1) or (number.start < gearPosition-1 and number.end > gearPosition+2)):
		return True
	else:
		return False

class Number:
  def __init__(self, line, value, start, end):
    self.line = line
    self.value = value
    self.start = start
    self.end = end
    self.length = len(str(value))

class Gear:
  def __init__(self, line, start):
    self.line = line
    self.start = start

linecounter = 0
numbers = []
gears = []

for line in Lines:
	regex = re.finditer('\d+', line)
	for match in regex:
		newNumber = Number(linecounter, match[0], match.start(), match.end())
		numbers.append(newNumber)

	regex = re.finditer('\*', line)
	for match in regex:
		newGear = Gear(linecounter, match.start())
		gears.append(newGear)

	linecounter += 1

for gear in gears:
	neighbours = [item for item in numbers if (checkNumberAppropriateLine(item, gear.line) and checkNumberAppropriatePosition(item, gear.start))]
	if len(neighbours)==2:
		result += eval(neighbours[0].value) * eval(neighbours[1].value)

print(result)