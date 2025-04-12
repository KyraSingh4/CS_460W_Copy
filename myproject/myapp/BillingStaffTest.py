import unittest
from Member import BillingStaff

class TestBillingStaff(unittest.TestCase):
    def setUp(self):
        self.mem = BillingStaff()

    #def test_ModifyBill(self):
    #    self.assertTrue(self.mem.modifyBill(89, 'amount', 100))

    #def test_ModifyBillInvalidAttr(self):
    #    self.assertFalse(self.mem.modifyBill(89, 'test', '100'))

    #def test_ModifyBillInvalid(self):
    #    self.assertFalse(self.mem.modifyBill(False, False, False))

    #def test_DeleteCharge(self):
    #    self.assertTrue(self.mem.deleteCharge(89))

    #def test_DeleteChargeInvalid(self):
    #    self.assertFalse(self.mem.deleteCharge(False))

    #def test_modifyAnnualFee(self):
    #    self.assertTrue(self.mem.modifyAnnualFee(400))

    #def test_modifyAnnualFeeInvalid(self):
    #    self.assertFalse(self.mem.modifyAnnualFee(False))

    #def test_modifyGuestFee(self):
    #    self.assertTrue(self.mem.modifyGuestFee(5))

    def test_modifyGuestFeeInvalid(self):
        self.assertFalse(self.mem.modifyGuestFee(False))

    #def test_getBillingScheme(self):
    #    self.assertEqual(self.mem.getBillingScheme(), [(5,400)])

if __name__ == '__main__':
    unittest.main()