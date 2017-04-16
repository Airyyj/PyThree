from count import Count
import unittest

class TestSub(unittest.TestCase):
    '''减法测试'''
    def setUp(self):
        print("test case start")
    def test_sub(self):
        '''减法测试1'''
        j = Count(5,2)
        self.assertEqual(j.sub(),3)
    def test_sub2(self):
        '''减法测试2'''
        j = Count(6,2)
        self.assertEqual(j.sub(),4)

    def tearDown(self):
        print("test case end")