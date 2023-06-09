import random 

for num in range(2):
    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)
    sum = Dice1 + Dice2
    
    print("Rolling dice...")
    print('Die %d : %d ' %(Dice1, Dice2))
    if sum > 7:
        print('You won')
    else :
        print('You lost')