from count import Count
import unittest
class Testadd(unittest.TestCase):
    '''加法测试'''
    def setUp(self):
        print("test case startaa")

    def test_add(self):
        '''加法测试1'''
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        '''加法测试2'''
        j = Count(23,12)
        self.assertEqual(j.add(),35)
    def tearDown(self):
        print("test case endaa")