import unittest
class SkipDemo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    #@unittest.skip(reason)  无条件跳过装饰的测试
    @unittest.skip('直接跳过测试')
    def test_skip(self):
        print("test_skip")
    #@unittest.skipIf(condition,reason),如果条件为真时，跳过装饰的测试
    @unittest.skipIf(3>1,"当条件为True时跳过测试")
    def test_skip_if(self):
        print("test_skip_if")
    #unittest.skipUnless(condition,reason)跳过装饰的测试，除非条件为真
    @unittest.skipUnless(3>2,"当条件为True时执行测试")
    def test_skip_unless(self):
        print("test_skip_unless")
    #标记为失败，不管执行结果是否失败，统一标记为失败。
    @unittest.expectedFailure
    def test_expected_failure(self):
        assertEqual(2,3)

if __name__ == '__main__':
    unittest.main()
