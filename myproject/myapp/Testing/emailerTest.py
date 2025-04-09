import unittest
from unittest.mock import patch, MagicMock
from myapp.emailer import Emailer

class TestEmailer(unittest.TestCase):

    def setUp(self):
        self.emailer = Emailer()
