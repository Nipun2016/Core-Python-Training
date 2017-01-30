def play_game(player,computer):
    if (player == "rock" and computer == "sissor"):
        return ("congratulation!.....player win ")
    elif (player == "sissor" and computer == "rock"):
        return ("congratulation!.....Computer win")
    elif (player == "sissor" and computer == "paper"):
        return ("congratulation!.....player win")
    elif (player == "paper" and computer == "sissor"):
        return ("congratulation!.....Computer win")
    elif (player == "paper" and computer == "rock"):
        return ("congratulation!.....player win")
    elif (player == "rock" and computer == "paper"):
        return ("congratulation!.....Computer win")
    elif (player == computer):
        return ("Match Draw..")
    else:
        return("Enter valid Inputs")

if __name__ == "__main__":
    repeat = "y"

    while repeat == "y":
        player = input("Enter Player choice (rock/paper/sissor) : ")
        comp = input("Enter Computer choice (rock/paper/sissor) : ")
        print (play_game(player,comp))
        repeat = input("Do you want to continue??? (y/n) ")
