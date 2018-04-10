import random  as ran
import matplotlib.pylab as plt
def roll_dice():
    dice = ran.randint(1,100)
    if dice in range(1,50):
        #print(str(dice)+" house wins")
        return False
    elif dice in range(51,99):
        #print(str(dice)+" you win!")
        return True
    else:
        #print(str(dice)+"you lost")
        return False
#this function will bet in dice rolling
#funds is the base amount
#init_wager is the amount of bet
#wage_count for each init_wager, how many time we want to roll the dice
def Bettor(funds,init_wager,wage_count):
    global bankrupt
    value = funds
    wage = init_wager
    curr_wager = 1
    wX = []  # current wager
    vY = [] #the value
    while curr_wager < wage_count:

        if roll_dice():
            value += wage
            wX.append(curr_wager)
            vY.append(value)
        else:
            value -= wage
            wX.append(curr_wager)
            vY.append(value)
        curr_wager += 1
    if value < 0:
        value = 'broke'
        bankrupt += 1
    print("\nthe fund is:"+str(value))
    plt.plot(wX,vY)
#we are iterating x because we are betting x times 
bankrupt = 0
x = 1
while x <= 10:
    Bettor(10000, 1000, 100)
    x += 1
print(('death rate:',(bankrupt/float(x)) * 100))
print(('survival rate:',100 - ((bankrupt/float(x)) * 100)))
plt.xlabel("wage_count")
plt.ylabel("value")
plt.axhline(1, color = 'r')
plt.savefig("bettor_result2.svg")
