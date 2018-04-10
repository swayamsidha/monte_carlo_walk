#04:50:20  IST 
import random as rnd
import matplotlib.pyplot as plt
def roll_dice():
	dice = rnd.randint(1,100)
	if dice in range(1,50):
		return False
	elif dice in range(50,99):
		return True
	elif dice == 100:
		return False
def martingale(funds, init_wager, wage_count):
	global bankrupt
	value = funds
	wager = init_wager
	
	wX = []
	vY = []
	
	curr_wager = 1
	
	#we are betting based on previous wager
	prev_wager = 'win'
	
	prev_amt = init_wager
	while curr_wager <= wage_count:
		if prev_wager == 'win':
			if roll_dice():
				value += wager
				#print('the value was'+str(value))
				wX.append(curr_wager)
				vY.append(value)
			else:
				value -= wager
				prev_wager = 'loss'
				#print('damn it was a loss')
				prev_amt = wager
				wX.append(curr_wager)
				vY.append(value)
				if value < 0:
					print('went bankrupt after'+str(curr_wager)+' bets')
					bankrupt += 1
					curr_wager += 1000000000000
		elif prev_wager == 'loss':
			#print('we v`e lost previous one')
			
			if roll_dice():
				wager = prev_amt * 2
				value += wager
				#print('we won')
				#print(value)
				wager = init_wager
				prev_wager = 'win'
				wX.append(curr_wager)
				vY.append(value)
			else:
				wager = prev_amt * 2
				#print('we lost'+str(wager))
				value -= wager
				prev_wager = 'loss'
				prev_amt = wager
				wX.append(curr_wager)
				vY.append(value)
				if value < 0:
					print('went bankrupt after'+str(curr_wager)+' bets')
					bankrupt += 1
					curr_wager += 1000000000000
					
					
		curr_wager += 1
	print(value)
	plt.plot(wX, vY)
bankrupt = 0
x = 1					
while x <= 10:				 
	martingale(10000,500,100)
	x += 1
print(('death rate:',(bankrupt/float(x)) * 100))
print(('survival rate:',100 - ((bankrupt/float(x)) * 100)))
plt.axhline(0, color = 'r')
plt.savefig('martingale_stat2.svg')



	
