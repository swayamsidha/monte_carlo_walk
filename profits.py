import random as rn
import matplotlib.pyplot as plt


def roll_dice():
	
	dice = rn.randint(1, 100)
	if dice in range(1, 50):
		return False
	elif dice == 100:
		return False
	elif dice in range(50, 100):
		return True

fortune = 500000
wager_size = 500
wager_count = 500

def martingale(funds, init_wager, count):
	global martin_brust
	global martin_profit
	value = funds
	wager = init_wager
	curr_wager = 1
	prev_wager = 'win'
	prev_amt = init_wager
	
	wX = []
	vY = []
	while curr_wager <= count:
		if prev_wager == 'win':
			if roll_dice():
				value += wager
				wX.append(curr_wager)
				vY.append(value)
			else:
				value -= wager
				prev_wager = 'loss'
				prev_amt = wager
				wX.append(curr_wager)
				vY.append(value)
				if value <= 0:
					curr_wager += 100000000000
					martin_brust += 1
		elif prev_wager == 'loss':
			if roll_dice():
				wager = prev_amt * 2
				if(value - wager) <= 0:
					wager = value
				value += wager
				wager = init_wager
				prev_wager = 'win'
				
				wX.append(curr_wager)
				vY.append(value)
			else:
				wager = prev_amt * 2
				
				if(value - wager) < 0:
					wager = value
				value -= wager
				prev_wager = 'loss'
				prev_amt = wager
				wX.append(curr_wager)
				vY.append(value)
				
				if value <= 0:
					curr_wager += 1000000000000
					martin_brust += 1
		curr_wager += 1
	plt.plot(wX,vY)
	if value > funds:
		martin_profit += 1
def simple_stat(fund, init_wager, count):
	
	global simple_brust
	global simple_profit
	
	value = fund
	wager = init_wager
	
	wX = []
	vY = []
	curr_wager = 1
	while curr_wager <= count:
		if roll_dice():
			value += wager
			wX.append(curr_wager)
			vY.append(value)
		else:
			value -= wager
			wX.append(curr_wager)
			vY.append(value)
			if value <= 0:
				curr_wager += 1000000000000
				simple_brust += 1
		curr_wager += 1
	plt.plot(wX, vY, 'k')
	if value > fund:
		simple_profit += 1
x = 0
simple_brust = 0.0
simple_profit = 0.0
martin_brust = 0.0
martin_profit = 0.0

while x < 1000:
	simple_stat(fortune, wager_size, wager_count)
	martingale(fortune, wager_size, wager_count)
	x += 1
print('martingale profit chances : '+str((martin_profit/1000) * 100))
print('martingale brust chances : '+str((martin_brust/1000) * 100))
print('simple profit chances : '+str((simple_profit/1000) * 100))
print('simple brust chances : '+str((simple_brust/1000) * 100))
plt.axhline(1, color = 'r')
plt.xlabel('current wager')
plt.ylabel('value')
plt.savefig('compare_profit.svg')
