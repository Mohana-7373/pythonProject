import unittest
from student import student

class Teststudent(unittest.TestCase):
    def test_email(self):
        obj = student("yamani", "yeddula", 60)
        self.assertEqual(obj.email,"yamani.yeddula@gmail.com")
        obj.first = "charan"
        self.assertEqual(obj.email,"charan.yeddula@gmail.com")
    def test_fullname(self):
        obj = student("yamani","yeddula",60)
        self.assertEqual(obj.fullname,("yamani yeddula"))
        obj.first = "charan"
        self.assertEqual(obj.fullname,("charan yeddula"))

    def test_bonus(self):
        obj = student("yamani","yeddula", 60)
        self.assertEqual(obj.marks, 60, 60)
        obj.apply_bonus()
        self.assertEqual(obj.marks,90, 90)

   # def test_updatevalue(self):
    #    obj = student("yamani","yeddula",30)
     #   self.assertEqual(obj.marks, 30, 30)
      #  obj.somevalue()
       # self.assertEqual(obj.marks, 90, 90)
    def test_somevalue(self):
        obj = student("yamani","yeddula",50)
        self.assertEqual(obj.value, "")
        obj.somevalue("mani")
        self.assertEqual(obj.value, "yamani.yeddula@gmail.comyamani yeddulamani")




if __name__ == "__main__":
    unittest.main()