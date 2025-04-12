import unittest
import datetime
from CS_460W.myproject.myapp.Bill import Bill

class testBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(1)

    #def test_get_total(self):
    #    self.assertEqual(self.bill.getTotal(), 430)

    #def test_get_charge_positive(self):
    #    #self.assertIsNone(self.bill.createCharge(20, 'test charge', 'test'))
    #    pass

    #def test_get_charge_invalid_input(self):
    #   self.assertFalse(self.bill.createCharge('test', 20, False))

    #def test_createChargeWrongMember(self):
    #    b2 = Bill(10)
    #    self.assertEqual(b2.createCharge(20, 'Test', 'Test'), -1)

    #def test_pay_bill(self):
    #    self.assertIsNone(self.bill.payBill(2025))

    #def test_pay_bill_invalid(self):
    #    self.assertFalse(self.bill.payBill('False'))

    #def testGetBill(self):
    #    self.assertEqual(self.bill.getBill(), [(76, 100.0, datetime.date(2024, 5, 5), 'Unpaid from LY', 'Other'),(74, 400.0, datetime.date(2025, 4, 10), 'Annual', 'Annual'),('', 500.0, '', 'Total Bill', '')])

    #def testGetFullBill(self):
    #    self.assertEqual(self.bill.getFullBill(),[(76, 100.0, datetime.date(2024, 5, 5), 'Unpaid from LY', 'Other'),(74, 400.0, datetime.date(2025, 4, 10), 'Annual', 'Annual'),(77, 50, datetime.date(2025, 4, 11),'Paid Charge', 'Other'),('', 500.0, '', 'Total Bill', '')])

    def testGetFullBill(self):
        b3 = Bill('test')
        self.assertFalse(b3.getFullBill())

if __name__ == '__main__':
    unittest.main()
