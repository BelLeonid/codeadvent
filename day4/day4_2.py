import re

result = 0

file1 = open('text1.txt', 'r')
Lines = file1.readlines()

class cardData:
    def __init__(self, wins):
        self.wins = wins
        self.number = 1

cardWinnings = []

for line in Lines:
	counter = 0
	dataLine = line.split(": ")[1].split("|")
	winningNumbers = dataLine[0]
	myNumbers = dataLine[1]
	regexWin = re.findall('\d+', winningNumbers)
	regexMy = re.findall('\d+', myNumbers)
	for testNumber in regexWin:
		if testNumber in regexMy:
			counter+=1
	cardWinnings.append(cardData(counter))

for index, data in enumerate(cardWinnings):
	for x in range(data.wins):
		if index+x+1 >= len(cardWinnings):
			break
		cardWinnings[index+x+1].number+=data.number
	result+=data.number
print(result)