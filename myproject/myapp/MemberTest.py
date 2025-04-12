import unittest
from Member import Member
import datetime

class TestMember(unittest.TestCase):
    def setUp(self):
        self.mem = Member(5)

    #def test_getInformation(self):
    #    self.assertEqual(self.mem.getInformation(), [('President', 'Staff', 'president@aced.com','111-111-1111', False, 4)])

    #def test_UpdateInformationPositive(self):
    #    self.assertIsNone(self.mem.updateInformation('firstname', 'Alex'))

    #def test_GetInformationInvalidAttr(self):
    #    self.assertFalse(self.mem.updateInformation('Test', 'Alex'))

    #def test_GetInformationInvalidType(self):
    #    self.assertFalse(self.mem.updateInformation(123, 'Alex'))

    #def test_ReservationRulesC1(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(15,00,00), datetime.time(16,00,00), 8, [2],[]), 0)

    #def test_ReservationRulesC2(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(11,30,00), datetime.time(12,30,00), 1, [2],[]), 1)

    #def test_ReservationRulesC3(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(11,30,00), datetime.time(12,30,00), 7, [2],[]), 2)

    #def test_ReservationRulesC4(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(9,30,00), datetime.time(10,30,00), 5, [2],[]), 3)

    #def test_ReservationRulesC5(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(12,30,00), datetime.time(1,30,00), 5, [2],[]), 4)

    #def test_ReservationRulesC6(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 10, datetime.time(12,30,00), datetime.time(1,30,00), 5, [2],[]), 5)

    #def test_ReservationRulesC7(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(15,00,00), datetime.time(16,00,00), 5, [],['Guest Pass']), 6)

    #def test_ReservationRulesC8(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 6, datetime.time(15,00,00), datetime.time(16,00,00), 5, [2], []), 7)

    #def test_ReservationRulesC9a(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 0, datetime.time(15,00,00), datetime.time(16,00,00), 5, [2,3],[]), 8)

    #def test_ReservationRulesC9b(self):
    #    self.assertEqual(self.mem.checkReservationRules('doubles', 0, datetime.time(15,00,00), datetime.time(16,30,00), 5, [2,3,4,5],[]), 8)

    #def test_ReservationRulesC10a(self):
    #    self.assertEqual(self.mem.checkReservationRules('singles', 0, datetime.time(15,00,00), datetime.time(17,00,00), 5, [2],[]), 9)

    #def test_ReservationRulesC10b(self):
    #    self.assertEqual(self.mem.checkReservationRules('doubles', 6, datetime.time(15,00,00), datetime.time(16,00,00), 5, [2,3,4],[]), 9)

    #def test_ReservationRulesInvalid(self):
    #    self.assertFalse(self.mem.checkReservationRules('singles', False, datetime.time(15,00,00), datetime.time(16,00,00), 5, [2],[]))

    #def test_CreateReservation(self):
    #    self.assertTrue(self.mem.createReservation('doubles', 6, datetime.time(15,00,00), datetime.time(16,30,00), 8, [2,3], ['Ryder Raymond']))

    #def test_CreateReservationInvalid(self):
    #    self.assertFalse(self.mem.createReservation('doubles', False, datetime.time(15,00,00), datetime.time(16,30,00), 8, [2,3], ['Ryder Raymond']))

    #def test_UpdateReservation(self):
    #    self.assertIsNone(self.mem.updateReservation(38, ['Kyra Singh', 'Bri Durso', 'Bas Asad']))

    def test_updateReservationInvalidPlayers(self):
        self.assertFalse(self.mem.updateReservation(38,['Kyra Singh']))

    def test_updateReservationInvalidID(self):
        self.assertFalse(self.mem.updateReservation(34, ['Kyra Singh']))

    def test_updateReservationInvalidType(self):
        self.assertFalse(self.mem.updateReservation(38,1))

if __name__ == '__main__':
    unittest.main()