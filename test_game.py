import unittest
from unittest.mock import patch
from io import StringIO
import game

class TestGame(unittest.TestCase):

##############################
# welcome_message() -> None
############################## 
	@patch('sys.stdout', new_callable=StringIO)
	def test_welcome_message(self, mock_stdout):
		game.welcome_message()
		assert mock_stdout.getvalue() == "\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nTry to guess the number!\n"

##############################
# choose_difficulty() -> str
############################## 
	@patch('game.input', return_value='1')
	def test_choose_difficulty(self, input):
		self.assertEqual(game.choose_difficulty(), 'Easy')

	@patch('game.input', return_value='2')
	def test_choose_difficulty_2(self, input):
		self.assertEqual(game.choose_difficulty(), 'Medium')

	@patch('game.input', return_value='3')
	def test_choose_difficulty_3(self, input):
		self.assertEqual(game.choose_difficulty(), 'Hard')
	
	@patch('game.input', create=True)
	def test_choose_difficulty_4(self, mocked_input):
		mocked_input.side_effect = ['h', 'dasda', '1']
		self.assertEqual(game.choose_difficulty(), 'Easy')

##############################
# num_randomizer() -> int
############################## 
	@patch('game.random')
	def test_num_randomizer(self, mock_random):
		mock_random.randint.return_value = 74
		self.assertEqual(game.num_randomizer(), 74)

##############################
# game_logic(difficulty, target_num) -> list[bool, int, int]
############################## 
	@patch('game.input', create=True)
	def test_game_logic(self, mocked_input):
		mocked_input.side_effect = ['asdas', 'h', 'h', '1', '2', 'h', '3']
		self.assertEqual(game.game_logic("Hard", 3), [True, 3, 2])
	
	@patch('game.input', create=True)
	def test_game_logic_2(self, mocked_input):
		mocked_input.side_effect = ['h', '1', '2', 'hhhh', '3', 'ada', '4', '5']
		self.assertEqual(game.game_logic("Medium", 5), [True, 5, 1])

	@patch('game.input', create=True)
	def test_game_logic_3(self, mocked_input):
		mocked_input.side_effect = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '!!--', '10']
		self.assertEqual(game.game_logic("Easy", 10), [True, 10, 0])
	
	@patch('game.input', create=True)
	def test_game_logic_4(self, mocked_input):
		mocked_input.side_effect = ['asdas', 'h', 'h', '1', '2', 'h', '4']
		self.assertEqual(game.game_logic("Hard", 3), [False, -1, -1])

##############################
# check_time() -> float
##############################
	@patch('game.time')
	def test_check_time(self, mock_time):
		mock_time.time.return_value = 1745630285.9581666
		self.assertEqual(game.check_time(), 1745630285.9581666)
		print()

##############################
# round_time(time) -> int
##############################
	def test_round_time(self):
		self.assertEqual(game.round_time(15), 15)
		self.assertEqual(game.round_time(15.499999), 15)
		self.assertEqual(game.round_time(14.500001), 15)
		self.assertEqual(game.round_time(14.9), 15)

##############################
# time_message(rounded_time) -> str 
##############################
	def test_time_message(self):
		self.assertEqual(game.time_message(15), "It took you 15 seconds to guess the answer!")

	def test_time_message_2(self):
		self.assertEqual(game.time_message(0), "It took you 0 seconds to guess the answer!")

##############################
# loser_message() -> str
##############################
	def test_loser_message(self): 
		self.assertEqual(game.loser_message(), "You lose! You ran out of chances.")

##############################
# get_guess(hint_num, target_num) -> list[int, int]
##############################
	@patch('game.input', return_value='2')
	def test_get_guess(self, input):
		self.assertEqual(game.get_guess(0, 74), [0, 2])
	
	@patch('game.input', return_value='76')
	def test_get_guess_2(self, input):
		self.assertEqual(game.get_guess(0, 74), [0, 76])
	
	@patch('game.input', create=True)
	def test_get_guess_3(self, mocked_input):
		mocked_input.side_effect = ['0', '1']
		self.assertEqual(game.get_guess(0, 74), [0, 1])

	@patch('game.input', create=True)
	def test_get_guess_3(self, mocked_input):
		mocked_input.side_effect = ['101', '73']
		self.assertEqual(game.get_guess(0, 74), [0, 73])

	@patch('game.input', create=True)
	def test_get_guess_5(self, mocked_input):
		mocked_input.side_effect = ['ergh', 'h', '0', '101', 'h', '100']
		self.assertEqual(game.get_guess(0, 74), [2, 100])

##############################
# get_hint(hint_num, target_num) -> list[str, bool]
##############################
	def test_get_hint(self):
		self.assertEqual(game.get_hint(0, 15), ["The target is odd", True])

	def test_get_hint_2(self):
		self.assertEqual(game.get_hint(0, 16), ["The target is even", True])

	def test_get_hint_3(self):
		self.assertEqual(game.get_hint(1, 15), ["The target numbers last digit is 5", True])
	
	def test_get_hint_4(self):
		self.assertEqual(game.get_hint(1, 90), ["The target numbers last digit is 0", True])

	def test_get_hint_5(self):
		self.assertEqual(game.get_hint(2, 90), ["No more hints..", False])

##############################
# check_guess(target_num, user_guess) -> list[str, bool]
##############################
	def test_check_guess(self):
		self.assertEqual(game.check_guess(74, 73), ["Incorrect! The number is greater than 73.", False])
	
	def test_check_guess_2(self):
		self.assertEqual(game.check_guess(74, 75), ["Incorrect! The number is less than 75.", False])

	def test_check_guess_3(self):
		self.assertEqual(game.check_guess(1, 1), ["", True])
	
##############################
# winner_message(guess_attempt, hints_used) -> list[str, bool]
##############################
	def test_winner_message(self):
		self.assertEqual(game.winner_message(9, 2), "Congratulations! You guessed the correct number in 9 attempts!\nYou used 2 hints!")

##############################
# play_again() -> bool
##############################
	@patch('game.input', return_value='y')
	def test_play_again(self, input):
		self.assertEqual(game.play_again(), True)

	@patch('game.input', return_value='n')
	def test_play_again_2(self, input):
		self.assertEqual(game.play_again(), False)

	@patch('game.input', create=True)
	def test_play_again_3(self, mocked_input):
		mocked_input.side_effect = ['dasdasda', '75', 'h', 'as', 'y']
		self.assertEqual(game.play_again(), True)

##############################
# goodbye_message() -> str
##############################
	def test_goodbye_message(self):
		self.assertEqual(game.goodbye_message(), "Thank you for playing! Have a nice day.\n")

##############################
# main() -> None
##############################
	@patch('game.input', create=True)
	@patch('game.random')
	def test_main(self, mock_random, mocked_input):
		mocked_input.side_effect = ['adsad', '3', '1', '1', 'n']
		mock_random.randint.return_value = 1
		game.main()
	
	@patch('game.input', create=True)
	@patch('game.random')
	def test_main_2(self, mock_random, mocked_input):
		mocked_input.side_effect = ['adsad', '2', 'dasd', 'h', 'h', '59', '79', '89', '99', 'n']
		mock_random.randint.return_value = 99
		game.main()
	
	@patch('game.input', create=True)
	@patch('game.random')
	def test_main_2(self, mock_random, mocked_input):
		mocked_input.side_effect = ['adsad', '1', 'dasd', 'h', 'h', '1', '2', 'h', '3', '4', '5', '6', '7', '8', '9', '10', 'n']
		mock_random.randint.return_value = 53
		game.main()
	
	@patch('game.input', create=True)
	@patch('game.random')
	def test_main_3(self, mock_random, mocked_input):
		mocked_input.side_effect = ['adsad', '3', 'dasd', 'h', 'h', '1', '2', 'h', '3', 'y', '3', '4', '5', '6', 'y', '3', 'h', 'h', 'h', '7', '8', '9', 'n']
		mock_random.randint.return_value = 53
		game.main()
		
if __name__ == "__main__":
	unittest.main()

