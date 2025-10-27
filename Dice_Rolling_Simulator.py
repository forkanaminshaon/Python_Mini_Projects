
#Python Dice Rolling Simulator

import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1, 6))
    PlayAgain = input("Do you want to Roll Again? (yes/no): ")
    if PlayAgain.lower() != "yes":
        continue
    else :
        break
print("Thank you for playing the Dice Rolling Simulator!")