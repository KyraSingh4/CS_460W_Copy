import unittest
from CS_460W.myproject.myapp.Authenticator import Authenticator

class TestAuthenticator(unittest.TestCase):

    def setUp(self):
        self.auth = Authenticator()

    def test_login_pos(self):
        self.assertEqual(self.auth.login('PStaf', 'ilovetennis'), 1, 'It bork')

    def test_login_invalid(self):
        self.assertFalse(self.auth.login('PStaf','ihatetennis'),'It bork')

    def test_login_invalid_input(self):
        self.assertFalse(self.auth.login(1, False), 'Fail')


if __name__ == '__main__':
    unittest.main()