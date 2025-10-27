#Python Text Based Adventure Game

answer = input("Do you want to play a game? [Yes/No]:")

if answer == "Yes":
    print("Welcome to the game!!!")
    answer = input("Do you want to go jungle or cave? [Jungle/Cave]:")
    if answer == "Jungle":
        print("You see the hungry tiger, you have to run away!")
    elif answer == "Cave":
        print("You seen the bear in front of the cave!")
        answer = input("Do you want to fight with the bear or run away? [Fight/Run]:")
        if answer == "Fight":
            print("You fought bravely but the bear was too strong. You lost bro!")
        elif answer == "Run":
            print("You are alive bro.")
            
else:
    print("The game closed")