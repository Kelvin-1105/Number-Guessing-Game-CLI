import random
import time

def welcome_message() -> None: ###
	print("\nWelcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	print("Try to guess the number!")

def choose_difficulty() -> str: ###
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

def num_randomizer() -> int: ###
	return random.randint(1, 100)

def game_logic(difficulty: str, target_num: int) -> list[bool, int, int]:
	print(f"\nGreat! You have selected the {difficulty} difficulty level.")
	print("Let's start the game!")
	print("(Enter h for a hint..)")
	hint_num = 0

	chances_dict = {'Easy': 10, 'Medium': 5, 'Hard': 3}
	for i in range(0, chances_dict[difficulty]):
		hint_num, user_guess = get_guess(hint_num, target_num)
		guess_message, is_winner = check_guess(target_num, user_guess)
		None if is_winner else print(guess_message)
		if is_winner:
			return [True, i+1, hint_num]
	return [False, -1, -1]

def check_time() -> float: ###
	return time.time()

def round_time(time: float) -> int: ###
	return int(time + 0.5)

def time_message(rounded_time: int) -> str: ###
	return f"It took you {rounded_time} seconds to guess the answer!"

def loser_message() -> str: ###
	return "You lose! You ran out of chances."

def get_guess(hint_num: int, target_num: int) -> list[int, int]: 
	user_guess = -1
	while True:
		user_guess = input("\nEnter your guess: ")
		if user_guess == 'h':
			hint, increment_hint = get_hint(hint_num, target_num)
			print(hint)
			if increment_hint: hint_num += 1
		elif not user_guess.isnumeric():
			print("Please select a number 1 through 100")
		elif int(user_guess) < 1 or int(user_guess) > 100:
			print("Please select a number 1 through 100")
		else: 
			return [hint_num, int(user_guess)] # change order

def get_hint(hint_num: int, target_num: int) -> list[str, bool]: ###
	hint_num += 1
	if hint_num == 1:
		parity = "even" if target_num % 2 == 0 else "odd"
		return [f"The target is {parity}", True]
	elif hint_num == 2:
		return [f"The target numbers last digit is {target_num % 10}", True]
	else:
		return ["No more hints..", False]

def check_guess(target_num: int, user_guess: int) -> list[str, bool]: ###
	if target_num > user_guess:
		return [f"Incorrect! The number is greater than {user_guess}.", False]
	elif target_num < user_guess:
		return [f"Incorrect! The number is less than {user_guess}.", False]
	else:
		return ['', True]

def winner_message(guess_attempt: int, hints_used: int) -> str: 
	return f"Congratulations! You guessed the correct number in {guess_attempt} attempts!\nYou used {hints_used} hints!"

def play_again() -> bool: ###
	while True:
		play_again = input("\nWould you like to play again? [y]es or [n]o: ")
		if play_again != 'y' and play_again != 'n':
			print("Please respond with y or n")
		else: 
			return play_again == 'y'

def goodbye_message() -> str: 
	return "Thank you for playing! Have a nice day.\n"

def main() -> None: 
	welcome_message()
	is_playing = True
	while is_playing:
		difficulty = choose_difficulty()
		target = num_randomizer()

		start_time = check_time()
		is_win, user_attempts, hints_used = game_logic(difficulty, target)
		if is_win:
			print(winner_message(user_attempts, hints_used))
			print(time_message(round_time(check_time() - start_time)))
		else: 
			print(loser_message())

		if not play_again():
			print(goodbye_message())
			is_playing = False

if __name__ == "__main__":
	main()