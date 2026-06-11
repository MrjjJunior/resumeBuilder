import unittest
import coverage

from unittest.mock import patch
from updateResume import UpadateResume

class TestUpdateResume(unittest.TestCase):

    def setUp(self):
        self.updateResume = self.updateResume()


    def test_readResume(self):
        self.updateResume.readRume
        with self.assertRaises:
            FileNotFoundError
    

