import sys
from random import randint

# generate a number using randint and pass two values you want to randomize
answer = randint(int(sys.argv[1]), int(sys.argv[2]))


#check if input is 1 - 10. Use the while loop to keep guessing in case of wrong input
while True:
	try:
		# get input from user
		guess = int(input(f"Guess a number between {int(sys.argv[1])} to {int(sys.argv[2])}: "))
		if  0 < guess < 11:
			if int(guess) == answer:
				print("You're a genius")
				break
		else:
			print("It has to be 1 to 10")
	except ValueError:
		print("Please enter a number")
		continue