import unittest

class TestStringMethod(unittest.TestCase):
    def setUp(self):
        pass

    def test_strings_a(self):
        self.assertEqual('a'*4, 'aa')
    def test_string_concat(self):
        self.assertEqual("a"+"b", "ab")
    def test_upper(self):
        self.assertEqual('PYTHON'.upper(), 'PYTHON')
