import random 

print('What your name?')
name = input()
print('Hello. %s!' %name)
Dice1 = random.randint(1,6)
Dice2 = random.randint(1,6)
sum = Dice1 + Dice2
    
print("Rolling dice...")
print('Die %d : %d ' %(Dice1, Dice2))
print('Total value:')
print(sum)
if sum > 7:
    print('%s won' %name)
else :
    print('%s lost' %name)