#11:50:33  IST 
#comparison of basic stategy and martingale startegy
import random as rn
import matplotlib.pyplot as plt

fund = 10000
init_wager = 100
wage_count = 1000

#the dice function

def roll_dice():
	
	dice = rn.randint(1, 100)
	if dice in range(0,50):
		return False
	elif dice == 100:
		return False
	elif dice in range(50,100):
		return True
def stategy(fund, init_wager, wage_count, color):
	value = fund
	wager = init_wager
	wX = []
	vY = []
	currentWager = 1
	while currentWager <= wage_count:
		if roll_dice():
			value += wager
			wX.append(currentWager)
			vY.append(value)
		else:
			value -= wager
			wX.append(currentWager)
			vY.append(value)

			###add me
			if value < 0:
				currentWager += 10000000000000000
		currentWager += 1
	plt.plot(wX,vY,color)

x = 0
while x < 100:
	stategy(fund, init_wager, wage_count, 'k')
	stategy(fund, init_wager * 2, wage_count, 'c')
	x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.axhline(0, color = 'r')
plt.savefig('comp_stat.svg')
	
		
		
		
