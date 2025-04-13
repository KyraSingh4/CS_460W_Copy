import unittest
import Directory

class testDirectory(unittest.TestCase):
    def setUp(self):
        self.directory = Directory.Directory()

    #def test_searchAttr_pos(self):
    #    self.assertEqual(self.directory.searchAttr(4, 'phonenum', '555-555-5555'), [('Shalin', 'Singh', 'kyrals476@gmail.com', '555-555-5555')], "error")

    #def test_searchAttr_invalid(self):
    #    self.assertFalse(self.directory.searchAttr(4, 'email', 'invalidinput'))

    #def test_searchAttr_invalidattr(self):
    #    self.assertFalse(self.directory.searchAttr(4, 'invalid', 'Kyra'))

    #def test_nameLookup_pos(self):
    #    self.assertEqual(self.directory.nameLookup('Kyra', 'Singh'), 5, "error")

    def test_nameLookup_negative(self):
        self.assertFalse(self.directory.nameLookup('Test', 'Test'))

    # def test_getEmails_pos(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
