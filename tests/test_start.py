import unittest
from unittest.mock import patch

from start import Start


class TestStart(unittest.TestCase):
	@patch("builtins.input", return_value="1")
	def test_start_menu_returns_user_choice(self, mock_input):
		app = Start()
		choice = app.startMenu()

		self.assertEqual(choice, "1")
		mock_input.assert_called_once_with(" > ")

	
	@patch("builtins.input", return_value="2")
	def test_chocie(self, mock_input):
		app = Start()
		second = app.startMenu()

		self.assertEqual(second, "2")



if __name__ == "__main__":
	unittest.main()