import unittest
from ..Bill import Bill

class testBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(1)

    def test_get_total(self):
        self.assertEqual(self.bill.getTotal(), 410)

if __name__ == '__main__':
    unittest.main()