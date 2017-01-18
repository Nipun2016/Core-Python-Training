def play_game():
    player = input("Enter your choice from rock/paper/sissor")
    comp = input("Enter your choice from rock/paper/sissor")
    if (player == "rock" and comp == "sissor"):
        print ("congo!.....player win ")
    elif (player == "sissor" and comp == "rock"):
        print ("congo!.....comp win")
    elif (player == "sissor" and comp == "paper"):
        print ("congo!.....player win")
    elif (player == "paper" and comp == "sissor"):
        print ("congo!.....comp win")
    elif (player == "paper" and comp == "rock"):
        print ("congo!.....player win")
    elif (player == "rock" and comp == "paper"):
        print ("congo!.....comp win")
    else:
        print("Enter valid inputs")

    ans = input("Do you want to continue???")
    if(ans == 'y') or (ans == 'Y'):
        play_game()

play_game()
