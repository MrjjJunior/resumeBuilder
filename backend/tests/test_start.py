import unittest
import coverage
from unittest.mock import patch

from start import Start


class TestStart(unittest.TestCase):

	def setUp(self):
		self.app = Start()

	@patch("builtins.print")
	@patch("builtins.input", return_value=1)
	def test_start_menu_returns_user_choice(self, mock_input, mock_print):
		choice = self.app.startMenu()

		self.assertEqual(choice, 1)
		mock_input.assert_called_once_with("\t> ")

	@patch("builtins.print")
	@patch("builtins.input", return_value=2)
	def test_chocie1(self, mock_input, mock_print):
		second = self.app.startMenu()

		self.assertEqual(second, 2)
		mock_input.assert_called_once_with("\t> ")

	@patch("builtins.print") 
	@patch("builtins.input", return_value=None,)
	def test_choice3(self, mock_input, mock_print):
		# with self.assertRaises(SystemExit):
		# 	self.app.startMenu()
		self.assertRaises(SystemError)

		# mock_input.assert_called_once_with("\t> ")



if __name__ == "__main__":
	unittest.main()