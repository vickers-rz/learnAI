

# class Zhangsan:
#     '''
#     sadfasdfasdfa
#     '''
#     def __init__(self):
#         self.height = 180
#         self.weight = 140
#         self.age = 18
#
#     def say(self):
#         print('我要上大学')
#
# print(Zhangsan.__doc__)
#
#
# class Lisi(Zhangsan):
#     pass
#
# lisi = Lisi()
# print(lisi.height)
# print(lisi.weight)
# lisi.say()



# 当子类中存在与父类相同的属性或方法时，子类的属性或方法会优先调用自己的属性和方法
# 如果自己没有该属性或方法的时候，才会去父类中寻找
# class A:
#     a = 1
#     b = 2
#     c = 3
#
#     def say(self):
#         print('我是A')
#
#     def question(self):
#         print('你是谁')
#
# class B(A):
#     a = 4
#     b = 5
#
#     def say(self):
#         print('我是B')
#
# b = B()
# print(b.a)
# print(b.b)
# print(b.c)
#
# b.say()
# b.question()
# a = A()
# print(a.a)




# 类的多继承:多继承的属性和方法的访问顺序是按照继承顺序从左到右进行访问的
# 比如说，调用某方法时，会首先在自身的类中去寻找，如果自身的类没有这个方法，就会从继承的父类中去寻找
#
# class A:
#     a = 100
#     def say(self):
#         print('A')
#
#     def run(self):
#         print('我会跑步')
#
#
# class B:
#     a = 200
#     def say(self):
#         print('B')
#
#     def swim(self):
#         print('我会游泳')
#
# class C(A, B):
#     pass
#
# c = C()
# print(c.a)
# c.say()
# c.swim()
# print(C.mro())




# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def add(self):
#         return self.x + self.y
#
# class B(A):
#     def __init__(self, x, y, z):
#         A.__init__(self, x, y)
#         self.z = z
#
#     def add(self):
#         return A.add(self) + self.z
#
# a = A(1, 2)
# print(a.add())
# b = B(1, 2, 3)
# print(b.add())



# class A:
#     def __init__(self):
#         print('A')
#
# class B1(A):
#     def __init__(self):
#         A.__init__(self)
#         print('B1')
#
# class B2(A):
#     def __init__(self):
#         A.__init__(self)
#         print('B2')
#
#
# class C(B1, B2):
#     def __init__(self):
#         B1.__init__(self)
#         B2.__init__(self)
#         print('c')
#
# c = C()



# super()函数：根据mro继承顺序去搜索父类中的指定函数，并且自动绑定好self参数
# class A:
#     def __init__(self):
#         print('A')
#
# class B1(A):
#     def __init__(self):
#         super().__init__()
#         print('B1')
#
# class B2(A):
#     def __init__(self):
#         super().__init__()
#         print('B2')
#
#
# class C(B1, B2):
#     def __init__(self):
#         super().__init__()
#         print('c')
#
# c = C()


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('A')

    def add(self):
        print(self.x + self.y)

class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)
        print('B')

b = B(1, 2)
b.add()