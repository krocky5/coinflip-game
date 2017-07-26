import random 
## work in progress

def coinToss():
	number = 1
	recordList = []
	heads = 0 
	tails = 0 
	bet = input("Heads or Tails? (0 for Heads and 1 for Tails): ")
	for amount in range(int(number)):
		flip = random.randint(0,1)
		if (flip == 0):
			print("Heads")
			recordList.append("Heads")
		else:
			print("Tails")
			recordList.append("Tails")
	print(str(recordList))
	if (int(bet) == flip):
		print("win")
		print("you win ")
	else:
		print("lose")
		print("you guessed wrong")
coinToss()
