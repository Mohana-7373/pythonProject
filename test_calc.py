import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,20),30)
        self.assertEqual(calc.add(10.23,6.0),16.23)
    def test_sub(self):
        self.assertEqual(calc.sub(5,3),2)
        self.assertEqual(calc.sub(50,40),10)
    def test_mul(self):
        self.assertEqual(calc.mul(2,3),5)
    def test_div(self):
        self.assertEqual(calc.div(10,5),2)
    def setup(self):
        print("\nsetup")

    def teardown(self):
        print("\nteardown")
if  __name__ == "__main__":
    unittest.main()