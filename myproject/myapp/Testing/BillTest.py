import unittest
import datetime
from ..Bill import Bill

class testBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(1)

    #def test_get_total(self):
    #    self.assertEqual(self.bill.getTotal(), 430)

    #def test_get_charge_positive(self):
    #    self.assertIsNone(self.bill.createCharge(20, 'test charge', 'test'))

    #def test_get_charge_invalid_input(self):
    #    self.assertFalse(self.bill.createCharge('test', 20, False))

    #def test_pay_bill(self):
    #    self.assertIsNone(self.bill.payBill(2025))

    #def test_pay_bill_invalid(self):
    #    self.assertFalse(self.bill.payBill('False'))

    def testGetBill(self):
        self.assertEqual(self.bill.getBill(), [(76, 100.0, datetime.date(2024, 5, 5), 'Unpaid from LY', 'Other'),(74, 400.0, datetime.date(2025, 4, 10), 'Annual', 'Annual'),('', 500.0, '', 'Total Bill', '')])

    def testGetFullBill(self):
        self.assertEqual(self.bill.getFullBill(),[(76, 100.0, datetime.date(2024, 5, 5), 'Unpaid from LY', 'Other'),(74, 400.0, datetime.date(2025, 4, 10), 'Annual', 'Annual'),(77, 50, datetime.date(2025, 4, 11),'Paid Charge', 'Other'),('', 500.0, '', 'Total Bill', '')])


if __name__ == '__main__':
    unittest.main()
