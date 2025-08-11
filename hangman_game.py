import random

lives = 6
words = ['flower', 'garden', 'picnic', 'grass', 'fountain']
invalid_chars = [' ','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=',',','.','/','<','>','?','|']
secret_word = random.choice(words).upper()
display_list = ['_'] * len(secret_word)

print(f"Welcome to Hangman Game! \nYou have {lives} lives to guess the letters of the secret word. \nHave fun!")
print("\n")
print(f"Secret Word: {' '.join(display_list)}")

while lives > 0:
	guessed_letter = input("Enter a letter: ").upper()

	if guessed_letter in invalid_chars: 
		print("Invalid input! Please try again.")
		continue

	if guessed_letter not in secret_word:
		lives -= 1
		if lives == 0:
			print("Game Over :'(")
			print(f"The secret word is {secret_word}")
			break
		print(f"Oops, you have {lives} lives left. Please try again.")
		continue
	found_indeces = []
	for index in range (0, len(secret_word)):
		if secret_word[index] == guessed_letter:
			found_indeces.append(index)

	for position in found_indeces:
		display_list[position] = guessed_letter

	print(f"Secret Word: {' '.join(display_list)}")
	if '_' not in display_list:
		print("Congratulations! You found the secret word :)")
		break






