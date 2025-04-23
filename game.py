import random
import time

def welcome_message() -> None:
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	print("Try to guess the number!")

def choose_difficulty() -> str:
	print("\nPlease select the difficulty level:")
	print("1. Easy (10 Chances)")
	print("2. Medium (5 Chances)")
	print("3. Hard (3 Chances)")
	
	while True:
		difficulty = input("\nEnter your choice: ")
		if difficulty == '1':
			return 'Easy'
		elif difficulty == '2':
			return 'Medium'
		elif difficulty == '3':
			return 'Hard'
		else: 
			print("Please choose a number 1 through 3.")

def num_randomizer() -> int:
	return random.randint(1, 100)

def game_logic(difficulty: str, target: int) -> None:
	print(f"\nGreat! You have selected the {difficulty} difficulty level.")
	print("Let's start the game!")
	time = check_time()

	chances_dict = {'Easy': 10, 'Medium': 5, 'Hard': 3}
	for i in range(0, chances_dict[difficulty]):
		guess = user_guess()
		if check_guess(target, guess):
			winner_message(i+1)
			time = check_time(time)
			time_message(time)
			return
	loser_message()

def check_time() -> None:
	return time.time()

def check_time(time: float) -> int:
	rounded_time = round_time(check_time() - time)
	return rounded_time

def round_time(time: float) -> int:
	return int(time + 0.5)

def time_message(rounded_time: int):
	print(f"It took you {rounded_time} seconds to guess the answer!")

def loser_message() -> None:
	print("You lose! You ran out of chances.")

def user_guess() -> int:
	guess = -1
	while True:
		guess = input("\nEnter your guess: ")
		if not guess.isnumeric():
			print("Please select a number 1 through 100")
		elif int(guess) < 0 or int(guess) > 100:
			print("Please select a number 1 through 100")
		else: 
			return int(guess)

def check_guess(target: int, guess: int) -> bool:
	if target > guess:
		print(f"Incorrect! The number is greater than {guess}.")
	elif target < guess:
		print(f"Incorrect! The number is less than {guess}.")
	else:
		return True
	return False

def winner_message(guess_attempt: int) -> None:
	print(f"Congratulations! You guessed the target number in {guess_attempt} attempts.")

def play_again() -> bool:
	while True:
		ifAgain = input("\nWould you like to play again? [y]es or [n]o: ")
		if ifAgain != 'y' and ifAgain != 'n':
			print("Please respond with y or n")
		else: 
			return ifAgain == 'y'

def goodbye_message():
	print("\nThank you for playing! Have a nice day.\n")

def main(): 
	welcome_message()
	while True:
		difficulty = choose_difficulty()
		target = num_randomizer()

		game_logic(difficulty, target)
		if not play_again():
			goodbye_message()
			exit()
			
if __name__ == "__main__":
	main()