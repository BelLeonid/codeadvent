import re

result = 0

file1 = open('text2.txt', 'r')
Lines = file1.readlines()

for line in Lines:
	gamesArray = line.split(": ")
	regexId = re.findall('\d+', gamesArray[0])
	id = regexId[0]
	regexRed = ''.join(re.findall('\d+ red', gamesArray[1]))
	regexGreen = ''.join(re.findall('\d+ green', gamesArray[1]))
	regexBlue = ''.join(re.findall('\d+ blue', gamesArray[1]))

	regexRedNum = re.findall('\d+', regexRed)
	regexGreenNum = re.findall('\d+', regexGreen)
	regexBlueNum = re.findall('\d+', regexBlue)

	regexRedNum = [eval(i) for i in regexRedNum]
	regexGreenNum = [eval(i) for i in regexGreenNum]
	regexBlueNum = [eval(i) for i in regexBlueNum]
	if (max(regexRedNum) <= 12 and max(regexGreenNum) <= 13 and max(regexBlueNum) <= 14):
		result += eval(id)
	print(id, max(regexRedNum), max(regexGreenNum), max(regexBlueNum))
print(result)