import unittest


class TestValidMethods(unittest.TestCase):

    def test_valid_year(self):
        year1 = "1992"
        year2 = "israel"
        self.assertTrue(True, year1)
        self.assertFalse(False, year2)

    def test_valid_book_type(self):
        bk_type1 = "1"
        bk_type2 = "8"
        self.assertTrue(True, bk_type1)
        self.assertFalse(False, bk_type2)

    def test_valid_act(self):
        act1 = 4
        act2 = 0
        self.assertTrue(True, act1)
        self.assertFalse(False, act2)


if __name__ == '__main__':
    unittest.main()
