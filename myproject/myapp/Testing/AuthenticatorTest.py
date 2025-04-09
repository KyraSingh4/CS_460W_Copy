import unittest
from ..Authenticator import Authenticator

class TestAuthenticator(unittest.TestCase):

    def setUp(self):
        self.auth = Authenticator()

    def test_login_pos(self):
        self.assertEqual(self.auth.login('PStaf', 'ilovetennis'), 1, 'It bork')

    def test_login_invalid(self):
        self.assertFalse(self.auth.login('PStaf','ihatetennis'),'It bork')

    def test_login_invalid_input(self):
        with self.assertRaises(Exception):
            self.auth.login(1,1)


if __name__ == '__main__':
    unittest.main()