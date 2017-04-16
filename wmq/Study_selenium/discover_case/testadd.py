from count import Count
import unittest
class Testadd(unittest.TestCase):
    def setUp(self):
        print("test case startaa")

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(23,12)
        self.assertEqual(j.add(),35)
    def tearDown(self):
        print("test case endaa")