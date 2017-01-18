def game():
	user1 = raw_input("User 1 : ")
	user2 = raw_input("User 2 : ")

	if user1 == "Rock" and user2 == "Scissors" :
		print "Congratulation User 2 Wins..."
	elif user1 == "Paper" and user2 == "Scissors" :
		print "Congratulation User 2 Wins..."
	elif user1 == "Scissors" and user2 == "Paper" :
		print "Congratulation User 1 Wins..."
	elif user1 == "Paper" and user2 == "Rock" :
		print "Congratulation User 1 Wins..."
	elif user1 == "Rock" and user2 == "Paper" :
		print "Congratulation User 2 Wins..."
	elif user1 == "Scissors" and user2 == "Rock" :
		print "Congratulation User 1 Wins..."
	else:
		print "please enter right choice"
	
	repeat = raw_input("Do you want to Continue (y/n) : ")
	if (repeat == "y") or (repeat == 'Y'):
		game()
game()