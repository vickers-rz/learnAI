#定义了函数add
def add(a, b):
    return a + b

# 定义变量a和b
a = 1
b = 2

# 定义类Person
class Person:
    sno = 0
    def __init__(self, name,age):
        self.name = name
        self.age = age
        Person.sno += 1

    def show(self):
        print(f'{self.name} is {self.age} years old.学号是：{Person.sno}')
        print("This is moduleA")
        if __name__ == '__main__': # 判断当前模块是否被直接运行，如果是，则执行下面的代码
            print("And this is moduleA's __main__")
            """
            直接运行模块时：
            当一个 .py 文件被直接执行时，__name__ 的值会被设置为 "__main__"
            if __name__ == '__main__': 条件为真，会执行其中的代码块
            作为模块被导入时：
            当模块被其他文件通过 import 语句导入时，__name__ 的值是模块的实际名称
            if __name__ == '__main__': 条件为假，不会执行其中的代码块
            
            这种设计模式使得 moduleA.py 既可以作为独立脚本运行进行测试，
            也可以作为模块被其他文件安全地导入使用。
            """
if __name__ == '__main__':
    test = Person("aa",17)
    test.show()




def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

__all__ = ['a','add', 'sub', 'mul'] # 指定模块中哪些对象应该被导入,此处特意漏掉了div ，只针对 from 模块 import * 这种调用方法生效
"""
__all__ 是一个列表，用于指定模块中哪些对象应该被导入。
当使用 from module import * 时，Python 解释器会自动将 __all__ 中的对象导入到当前作用域。
"""
