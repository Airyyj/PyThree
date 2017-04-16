from calculator import Count
import unittest


'''

序号	断言方法	断言描述
1	assertEqual(arg1, arg2, msg=None)	验证arg1=arg2，不等则fail
2	assertNotEqual(arg1, arg2, msg=None)	验证arg1 != arg2, 相等则fail
3	assertTrue(expr, msg=None)	验证expr是true，如果为false，则fail
4	assertFalse(expr,msg=None)	验证expr是false，如果为true，则fail
5	assertIs(arg1, arg2, msg=None)	验证arg1、arg2是同一个对象，不是则fail
6	assertIsNot(arg1, arg2, msg=None)	验证arg1、arg2不是同一个对象，是则fail
7	assertIsNone(expr, msg=None)	验证expr是None，不是则fail
8	assertIsNotNone(expr, msg=None)	验证expr不是None，是则fail
9	assertIn(arg1, arg2, msg=None)	验证arg1是arg2的子串，不是则fail
10	assertNotIn(arg1, arg2, msg=None)	验证arg1不是arg2的子串，是则fail
11	assertIsInstance(obj, cls, msg=None)	验证obj是cls的实例，不是则fail
12	assertNotIsInstance(obj, cls, msg=None)	验证obj不是cls的实例，是则fail

assertEqual(first,second,msg=None) 断言第一个参数与第二参数是否相等，如果不想等则测试失败。
msg 为可选参数，用于定义测试失败是打印的信息。

'''


class TestCount(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j = Count(12,23)
        self.assertEqual(j.add(),35)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    #unittest.main()
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
