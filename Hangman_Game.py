word = "Shaon"
chances = 5
GuessADD = []

done = False

while not done:
    # Display current word progress
    for letter in word:
        if letter.lower() in GuessADD:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()  # Add newline for clarity

    Myguess = input(f"Your Chances are {chances}, Guess a letter: ").lower()

    # Prevent repeated guesses
    if Myguess in GuessADD:
        print("You already guessed that letter!")
        continue

    GuessADD.append(Myguess)

    # If wrong guess
    if Myguess not in word.lower():
        chances -= 1
        if chances == 0:
            print("\nYou Lost! The word was", word)
            done = True
    else:
        # Check if all letters are guessed
        if all(letter.lower() in GuessADD for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            done = True
print("Thank you for playing Hangman!")