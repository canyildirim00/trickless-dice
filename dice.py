import random

def dice(n):
    for i in range(n):
        dice = random.randint(1,6)
        print(dice)

n = int(input("How many dices do you want to throw? "))

dice(n)