import unittest
from myapp.emailer import Emailer

class TestEmailer(unittest.TestCase):

    def setUp(self):
        self.emailer = Emailer()

    def test_send_email_pos(self):
        self.emailer.connect()
        self.emailer.sendEmail("Hello World", "Test", "jhart@hartford.edu")

    def test_send_email_neg(self):
        with self.assertRaises(Exception):
            self.emailer.sendEmail("Hello World", "Test", "invalid_email")

if __name__ == '__main__':
    unittest.main()  # Run the tests