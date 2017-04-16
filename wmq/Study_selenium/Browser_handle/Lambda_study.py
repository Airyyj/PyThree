
from functools import reduce

#1 python lambda会创建一个函数对象，但不会把这个函数对象赋给一个标识符，而def则会把函数对象赋值给一个变量。
#2 python lambda它只是一个表达式，而def则是一个语句。
#匿名函数lambda
num = lambda x,y : x+y

print("lambda")
print(num(3,4))

#上面的代码可以使用 def 定义函数实现

def add(x,y):
    return x+y
print("def")
print(add(3,4))

'''
由上例可以看出
lambda的一般形式是关键字lambda后面跟一个或多个参数，
紧跟一个冒号，以后是一个表达式。
lambda是一个表达式而不是一个语句。
它能够出现在Python语法不允许def出现的地方。作为表达式，
lambda返回一个值（即一个新的函数）。
lambda用来编写简单的函数，而def用来处理更强大的任务。

'''

#lambda 使用举例
#python2 的用法
'''
#python2  是如下写法，但是python 3中修改了写法。见如下写法
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

#
print(filter(lambda x: x % 3 == 0, foo))
 #--[18, 9, 24, 12, 27]
map_list = list()
print(map(lambda x: x * 2 + 10, foo))
#--[14, 46, 28, 54, 44, 58, 26, 34, 64]
print(reduce(lambda x, y: x + y, foo))
'''





#python 3 的用法
#Python中，也有几个定义好的全局函数方便使用的，filter, map, reduce　　

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
num_list = list(filter(lambda x: x % 3 == 0, foo))
print(num_list)
 #--[18, 9, 24, 12, 27]
map_list = list(map(lambda x: x * 2 + 10, foo))
print(map_list)
#--[14, 46, 28, 54, 44, 58, 26, 34, 64]

'''
reduce函数：
在Python 3里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里 用的话要 先引
入：
'''
print(reduce(lambda x, y: x + y, foo))



# 下面的代码主要是为了 体现lambda 的其他用法，可以传递参数。而不使用的时候 不能传递参数

# Button(top, text="计算", command=lambda: on_click(top, base_text)).pack()
# top.mainloop()

# 这种 直接command = 方法名的方式，函数是不能传递参数的，所以为了能传递参数使用了上面的方法。
# Button(top, text="计算", command= on_click).pack()









