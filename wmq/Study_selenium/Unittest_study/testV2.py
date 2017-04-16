from calculator import Count
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

class TestAdd(MyTest):
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(23,12)
        self.assertEqual(j.add(),35)
class TestSub(MyTest):
    def test_sub(self):
        j = Count(5,2)
        self.assertEqual(j.sub(),3)
    def test_sub2(self):
        j = Count(6,2)
        self.assertEqual(j.sub(),4)

if __name__ == '__main__':
    unittest.main()