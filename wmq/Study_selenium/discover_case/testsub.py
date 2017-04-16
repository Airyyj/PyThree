from count import Count
import unittest

class TestSub(unittest.TestCase):

    def setUp(self):
        print("test case start")
    def test_sub(self):
        j = Count(5,2)
        self.assertEqual(j.sub(),3)
    def test_sub2(self):
        j = Count(6,2)
        self.assertEqual(j.sub(),4)

    def tearDown(self):
        print("test case end")