#Number Guessing Game

import random

RandomNumber = random.randrange(1, 200)

userInput = int(input("Guess the number:"))

if userInput > RandomNumber:
    print(RandomNumber)
    print("The number is too high")
    
elif userInput < RandomNumber:
    print(RandomNumber)
    print("The number is too low")

else:
    print(RandomNumber)
    print("Congratulations! You guessed the number correctly.") 
    
