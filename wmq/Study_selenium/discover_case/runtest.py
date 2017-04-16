import unittest

#discover(start_dir,pattern='test*.py,top_level_dir=None)
'''
找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件名才加载，
如果启动的不是顶层目录，那么顶层目录必须单独指定。
star_dir:要测试的模块名，或测试用例目录
pattern='test*.py':表示用例文件名的匹配原则。此处匹配文件名以‘test'开头的“.py”，类型的文件，星号“*”表示任意多个字符
top_level_dir=None:测试模块的顶层目录，如果没有顶层目录，默认为None
'''
#定义测试用例的目录为当前目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)