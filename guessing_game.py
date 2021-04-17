# I turned my guessing game into a module to be used in number_guess2.py

def guessing_game():
	"""Guess a random number"""
	import random
	import sys

	number = random.randint(1, 100)    # Generate a random number.
	again = 'yes'    # Resets play again to the 'yes' value. 
	count = 1     # Sets the number of tries to first try. Makes count of tries come out correctly.
	play_game = True 
	print(number)
	while play_game:
		guess = input("\nGuess a number between 1 and 100: ")
		guess = int(guess)

		if guess > number:
			print("Too high.")
			count += 1
		elif guess < number:
			print("Too low.")
			count +=1
		else:
			print(f"That's the number! It only took you {count} tries.")
			again = input("Do you want to play again? Enter 'yes' of 'no': ")


			if again == 'yes':
				guessing_game()
				
			else:
				sys.exit(0)