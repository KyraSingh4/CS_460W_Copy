import unittest
from Member import Member
import datetime

class TestMember(unittest.TestCase):
    def setUp(self):
        self.mem = Member(1)

    def test_getInformation(self):
        self.assertEqual(self.mem.getInformation(), [('President', 'Staff', 'president@aced.com','111-111-1111', False, 4)])

    #def test_UpdateInformationPositive(self):
    #    self.assertIsNone(self.mem.updateInformation('firstname', 'Alex'))

    #def test_GetInformationInvalidAttr(self):
    #    self.assertFalse(self.mem.updateInformation('Test', 'Alex'))

    #def test_GetInformationInvalidType(self):
    #    self.assertFalse(self.mem.updateInformation(123, 'Alex'))

    def test_ReservationRulesC1(self):
        self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(15,00,00), datetime.time(16,00,00), 8, [1],[]), 0)

    def test_ReservationRulesC2(self):
        self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(11,30,00), datetime.time(12,30,00), 1, [1],[]), 1)

    def test_ReservationRulesC3(self):
        self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(11,30,00), datetime.time(12,30,00), 7, [1],[]), 2)

    def test_ReservationRulesC4(self):
        self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(9,30,00), datetime.time(10,30,00), 7, [1],[]), 3)


if __name__ == '__main__':
    unittest.main()