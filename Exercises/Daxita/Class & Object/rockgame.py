def game(user1,user2):

	if user1 == "Rock" and user2 == "Scissors" :
		return ("Congratulation User 2 Wins...")
	elif user1 == "Paper" and user2 == "Scissors" :
		return ("Congratulation User 2 Wins...")
	elif user1 == "Scissors" and user2 == "Paper" :
		return ("Congratulation User 1 Wins...")
	elif user1 == "Paper" and user2 == "Rock" :
		return ("Congratulation User 1 Wins...")
	elif user1 == "Rock" and user2 == "Paper" :
		return ("Congratulation User 2 Wins...")
	elif user1 == "Scissors" and user2 == "Rock" :
		return ("Congratulation User 1 Wins...")
	elif user1 == user2:
		return ("Match Draw")
	else:
		return ("please enter right choice")
	
	repeat = input("Do you want to Continue (y/n) : ")
	if (repeat == "y") or (repeat == 'Y'):
		game()
	else:
		exit()

if __name__=="__main__":
	try:
		user1 = input("User 1 : ")
		if user1.isalpha():
			user2 = input("User 2 : ")
			print(game(user1,user2))
		else:
			print("Enter string")
	except Exception as e:
		print("Enter valid input")
