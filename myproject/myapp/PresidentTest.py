import unittest
from Member import President


class TestPresident(unittest.TestCase):

    def setUp(self):
        self.mem = President()

    #def test_AddEventFee(self):
    #    self.assertIsNone(self.mem.addEventFee(40, 'Test', 5))

    #def test_AddEventFeeInvalid(self):
    #    self.assertFalse(self.mem.addEventFee(False, False, False))

    #def test_CreateMember(self):
    #    self.assertIsNone(self.mem.createMember('John', 'Smith','jsmith@tennis.com','860-123-3456', True, 'Test'))

    #def test_CreateMemberInvalid(self):
    #    self.assertFalse(self.mem.createMember(False, False, False, False, 'False', False))

    def test_DeactivateMember(self):
        self.assertTrue(self.mem.deactivateMember(6))

    def test_DeactivateMemberIncorrectID(self):
        self.assertFalse(self.mem.deactivateMember(1))

    def test_DeactivateMemberInvalidInput(self):
        self.assertFalse(self.mem.deactivateMember(False))

if __name__ == '__main__':
    unittest.main()