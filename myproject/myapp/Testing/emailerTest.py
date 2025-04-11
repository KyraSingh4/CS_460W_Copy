import unittest
from unittest.mock import MagicMock
from CS_460W.myproject.myapp.emailer import Emailer

class TestEmailer(unittest.TestCase):

    def setUp(self):
        self.emailer = Emailer()

    def test_send_email_pos(self):
        self.emailer.connect()
        self.emailer.sendEmail("Hello World", "Test", "jhart@hartford.edu")

    def test_send_email_invalid_email(self):
        with self.assertRaises(Exception):
            self.emailer.sendEmail("Hello World", "Test", "invalid_email")

    def test_send_email_invalid_input(self):
        with self.assertRaises(Exception):
            self.emailer.sendEmail(123, 456, 789)

    def test_send_reservation_confirmation_pos(self):
        self.emailer.sendReservationConfirmation("1", "jhart@hartford.edu")

    def test_send_reservation_confirmation_invalid_email(self):
        with self.assertRaises(Exception):
            self.emailer.sendReservationConfirmation("1", "invalid_email")

    def test_send_reservation_confirmation_invalid_input(self):
        with self.assertRaises(Exception):
            self.emailer.sendReservationConfirmation(123, 456)

    def test_send_bill_email_pos(self):
        self.emailer.sendBillEmail([[1,400,"January 1st","Membership","Yearly Due"]],"jhart@hartford.edu")

    def test_send_bill_email_invalid_email(self):
        with self.assertRaises(Exception):
            self.emailer.sendBillEmail([[1,400,"January 1st","Membership","Yearly Due"]],"invalid_email")

    def test_send_bill_email_invalid_input(self):
        with self.assertRaises(Exception):
            self.emailer.sendBillEmail(123, 456)

    def test_late_bill_email_pos(self):
        self.emailer.lateBillEmail("jhart@hartford.edu")

    def test_late_bill_email_invalid_email(self):
        with self.assertRaises(Exception):
            self.emailer.lateBillEmail("invalid_email")

    def test_late_bill_email_invalid_input(self):
        with self.assertRaises(Exception):
            self.emailer.lateBillEmail(123)

if __name__ == '__main__':
    unittest.main()  # Run the tests