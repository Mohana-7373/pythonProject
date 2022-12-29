import unittest


class TestStringMethod(unittest.Testcase):
    def setUp(self):
        pass

    def test_strings_a(self):
        self.assertEqual('a' * 4, 'aa')
