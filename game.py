import random
import time

def welcome_message() -> None:
	print("\nWelcome to the Number Guessing Game!")
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

def game_logic(difficulty: str, target_num: int) -> None:
	print(f"\nGreat! You have selected the {difficulty} difficulty level.")
	print("Let's start the game!")
	print("(Enter h for a hint..)")
	start_time = check_time()
	hint_num = 0

	chances_dict = {'Easy': 10, 'Medium': 5, 'Hard': 3}
	for i in range(0, chances_dict[difficulty]):
		user_guess, hint_num = get_guess(hint_num, target_num)
		if check_guess(target_num, user_guess, i+1):
			time_message(round_time(check_time() - start_time))
			return
	loser_message()

def check_time() -> None:
	return time.time()

def round_time(time: float) -> int:
	return int(time + 0.5)

def time_message(rounded_time: int):
	print(f"It took you {rounded_time} seconds to guess the answer!")

def loser_message() -> None:
	print("You lose! You ran out of chances.")

def get_guess(hint_num: int, target_num: int) -> list[int, int]:
	user_guess = -1
	while True:
		user_guess = input("\nEnter your guess: ")
		if user_guess == 'h':
			hint(hint_num, target_num)
			hint_num += 1
		elif not user_guess.isnumeric():
			print("Please select a number 1 through 100")
		elif int(user_guess) < 0 or int(user_guess) > 100:
			print("Please select a number 1 through 100")
		else: 
			return [int(user_guess), hint_num]

def hint(hint_num: int, target_num: int) -> None:
	hint_num += 1
	if hint_num == 1:
		parity = "even" if target_num % 2 == 0 else "odd"
		print(f"The target is {parity}")
	elif hint_num == 2:
		print(f"The targets last digit is {target_num % 10}")
	else:
		print("No more hints..")

def check_guess(target_num: int, user_guess: int, guess_attempt: int) -> bool:
	if target_num > user_guess:
		print(f"Incorrect! The number is greater than {user_guess}.")
	elif target_num < user_guess:
		print(f"Incorrect! The number is less than {user_guess}.")
	else:
		winner_message(guess_attempt)
		return True
	return False

def winner_message(guess_attempt: int) -> None:
	print(f"Congratulations! You guessed the correct number in {guess_attempt} attempts!")

def play_again() -> bool:
	while True:
		play_again = input("\nWould you like to play again? [y]es or [n]o: ")
		if play_again != 'y' and play_again != 'n':
			print("Please respond with y or n")
		else: 
			return play_again == 'y'

def goodbye_message() -> None:
	print("Thank you for playing! Have a nice day.\n")

def main() -> None: 
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