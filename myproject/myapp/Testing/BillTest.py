import unittest
from ..Bill import Bill

class testBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(1)