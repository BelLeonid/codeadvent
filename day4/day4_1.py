import re

result = 0

file1 = open('text1.txt', 'r')
Lines = file1.readlines()

for line in Lines:
	counter = 0
	dataLine = line.split(": ")[1].split("|")
	winningNumbers = dataLine[0]
	myNumbers = dataLine[1]
	regexWin = re.findall('\d+', winningNumbers)
	regexMy = re.findall('\d+', myNumbers)
	for testNumber in regexWin:
		if testNumber in regexMy:
			if counter==0:
				counter=1
			else:
				counter=counter*2
	result+=counter
print(result)