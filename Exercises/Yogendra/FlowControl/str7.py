def game(play1,play2):
    play1=play1.lower() 
    play2=play2.lower()
    if play1=="rock" and play2=="scissors":
          con="n"
          return "player1"
    elif play1=="scissors" and play2=="rock":
          return "player2"
          con="n"
    elif play1=="paper" and play2=="rock":
          return "player1"
          con="n"
    elif play1=="rock" and play2=="paper":
          return "player2"
          con="n"
    elif play1=="scissors" and play2=="paper":
          return "player1"
          con="n"
    elif play1=="paper" and play2=="scissors":
          return "player2"
          con="n"
    elif play1==play2:
         return "tie"
         con="n"
    else:
         print("you have inputed wrong value")

if __name__=="__main__":
    con="y"
    while con=='y':
        print("you have on;y three choices--> 1.rock 2.paper 3.scissors")
        play1=input("Enter value value for player1: ")
        play2=input("Enter value value for player2: ")
        play1=play1.lower() 
        play2=play2.lower()
        game(play1,play2)
        print("you want to continue:")
        con=input("enter y to continu:")
