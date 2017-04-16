import unittest,time
from HTMLTestRunner import HTMLTestRunner

#指定测试用例为当前文件夹下的test_case目录
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = "./report/"+now+'_result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况：")
    runner.run(discover)
    fp.close()