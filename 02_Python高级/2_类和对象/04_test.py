
class Zhangsan:
    '''
    这是一个文档字符串（docstring），用于描述类的用途
    这个类代表张三，包含他的基本信息和行为
    '''
    def __init__(self):
        # __init__方法是类的构造函数，在创建对象时自动调用
        # self参数代表类的实例本身，必须是每个实例方法的第一个参数
        self.height = 180  # 身高属性，单位cm
        self.weight = 140  # 体重属性，单位斤
        self.age = 18      # 年龄属性，单位岁

    def say(self):
        # 定义一个实例方法，用于执行特定的行为
        print('我要上大学')  # 打印一句话

# 使用类名访问类的文档字符串
print(Zhangsan.__doc__)


# 演示类的继承概念
# Lisi类继承自Zhangsan类，意味着Lisi拥有Zhangsan的所有属性和方法
class Lisi(Zhangsan):
    # 使用pass关键字表示这个类没有额外的属性或方法
    # 但它会继承父类Zhangsan的所有内容
    pass

# 创建Lisi类的实例对象
lisi = Lisi()
# 通过子类实例访问从父类继承来的属性
print(lisi.height)  # 输出180
print(lisi.weight)  # 输出140
# 调用从父类继承来的方法
lisi.say()  # 输出"我要上大学"



# 当子类中存在与父类相同的属性或方法时，子类的属性或方法会优先调用自己的属性和方法
# 如果自己没有该属性或方法的时候，才会去父类中寻找
class A:
    a = 1  # 类属性
    b = 2  # 类属性
    c = 3  # 类属性

    def say(self):
        # 实例方法
        print('我是A')

    def question(self):
        # 实例方法
        print('你是谁')

class B(A):
    # 子类B重写了父类A的部分属性
    a = 4  # 重写父类的属性a
    b = 5  # 重写父类的属性b
    # 属性c没有重写，会继承父类的值

    def say(self):
        # 重写父类的方法say
        print('我是B')

# 创建B类的实例
b = B()
# 访问属性时，优先使用子类中定义的值
print(b.a)  # 输出4（子类B中的值）
print(b.b)  # 输出5（子类B中的值）
print(b.c)  # 输出3（从父类A继承的值）

# 调用方法时，优先使用子类中重写的方法
b.say()      # 输出"我是B"
b.question() # 输出"你是谁"（从父类A继承的方法）

# 创建A类的实例进行对比
a = A()
print(a.a)   # 输出1（父类A中的值）



# 类的多继承:多继承的属性和方法的访问顺序是按照继承顺序从左到右进行访问的
# 比如说，调用某方法时，会首先在自身的类中去寻找，如果自身的类没有这个方法，就会从继承的父类中去寻找

class A:
    a = 100
    def say(self):
        print('A')

    def run(self):
        # 跑步方法
        print('我会跑步')


class B:
    a = 200
    def say(self):
        print('B')

    def swim(self):
        # 游泳方法
        print('我会游泳')

# C类同时继承自A类和B类，这就是多继承
# 继承顺序很重要：先继承A，再继承B
class C(A, B):
    # C类没有定义自己的属性和方法，全部继承自父类
    pass

# 创建C类的实例
c = C()
# 当两个父类都有同名属性a时，按照继承顺序，优先使用第一个父类A的值
print(c.a)   # 输出100（来自类A）
# 当两个父类都有同名方法say时，按照继承顺序，优先使用第一个父类A的方法
c.say()      # 输出"A"（来自类A的方法）
# 只有类B有swim方法，所以直接使用
c.swim()     # 输出"我会游泳"

# 查看方法解析顺序（MRO: Method Resolution Order）
# 这显示了Python在多继承时查找方法的顺序
print(C.mro())  # 输出C类的方法解析顺序列表




class A:
    def __init__(self, x, y):
        # 带参数的构造函数
        self.x = x  # 实例属性x
        self.y = y  # 实例属性y

    def add(self):
        # 计算x和y的和
        return self.x + self.y

class B(A):
    def __init__(self, x, y, z):
        # 子类的构造函数需要调用父类的构造函数来初始化继承的属性
        A.__init__(self, x, y)  # 显式调用父类A的构造函数
        self.z = z  # 子类特有的属性z

    def add(self):
        # 重写父类的add方法，计算x、y、z三者的和
        return A.add(self) + self.z  # 调用父类的add方法，然后加上z
"""
这里的这个办法 A.add(self) 很重要！
"""

# 创建A类实例
a = A(1, 2)
print(a.add())  # 输出3 (1+2)

# 创建B类实例
b = B(1, 2, 3)
print(b.add())  # 输出6 (1+2+3)



class A:
    def __init__(self):
        # A类的构造函数
        print('A')  # 输出"A"

class B1(A):
    def __init__(self):
        # B1类的构造函数
        A.__init__(self)  # 调用父类A的构造函数
        print('B1')       # 输出"B1"

class B2(A):
    def __init__(self):
        # B2类的构造函数
        A.__init__(self)  # 调用父类A的构造函数
        print('B2')       # 输出"B2"


class C(B1, B2):
    def __init__(self):
        # C类的构造函数，需要手动调用所有父类的构造函数
        B1.__init__(self)  # 调用B1的构造函数
        B2.__init__(self)  # 调用B2的构造函数
        print('c')         # 输出"c"

# 创建C类实例，观察构造函数的调用顺序
c = C()



# super()函数：根据mro继承顺序去搜索父类中的指定函数，并且自动绑定好self参数
class A:
    def __init__(self):
        print('A')  # 输出"A"

class B1(A):
    def __init__(self):
        # 使用super()函数调用父类的构造函数
        # super()会根据MRO顺序自动找到合适的父类方法
        super().__init__()  # 调用父类A的构造函数
        print('B1')         # 输出"B1"

class B2(A):
    def __init__(self):
        # 使用super()函数调用父类的构造函数
        super().__init__()  # 调用父类A的构造函数
        print('B2')         # 输出"B2"


class C(B1, B2):
    def __init__(self):
        # 使用super()函数调用父类的构造函数
        super().__init__()  # 根据MRO顺序调用父类构造函数
        print('c')          # 输出"c"

# 创建C类实例，观察使用super()后的构造函数调用顺序
c = C()


class A:
    def __init__(self, x, y):
        # 带参数的构造函数
        self.x = x  # 实例属性x
        self.y = y  # 实例属性y
        print('A')  # 输出"A"

    def add(self):
        # 计算x和y的和并打印
        print(self.x + self.y)

class B(A):
    def __init__(self, a, b):
        # 子类构造函数调用父类构造函数，并传递参数
        super().__init__(a, b)  # 使用super()调用父类构造函数
        print('B')             # 输出"B"

b = B(1, 2)
b.add()
"""
这里，B类继承自A类，并定义了自己的构造函数。
在B类的构造函数中，我们首先调用了super()函数，然后调用了父类的构造函数，并传递了参数。
这样，B类就可以使用父类的属性和方法。
"""
