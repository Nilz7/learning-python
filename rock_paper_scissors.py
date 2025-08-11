import random

actions = ['rock', 'paper', 'scissors']

while True:
	
	user_action = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ")
	
	if user_action == "q":
		print("The game is ended.")
		break;
	elif user_action not in actions:
		print("You entered an invalid action! Please try again.")
		continue 

	computer_action = random.choice(actions)
	
	print(f"Your action is: {user_action}")
	print(f"Computer action is: {computer_action}")

	if user_action == computer_action:
		print("It's a tie!")
	elif (user_action == "rock" and computer_action == "scissors") or \
	(user_action == "paper" and computer_action == "rock") or \
	(user_action == "scissors" and computer_action == "paper"):
		print("You won!")
	else:
		print("You lost!")

