


# 类的定义
# class Person:
#     name = 'zhangsan'
#     age = 18
#     gender = 'nan'
#
#     def eat(self):
#         print('我会吃饭')
#
#     def drink(self):
#         print('我会喝水')

# 创建对象
# person = Person()
# 通过对象去调用类的属性和方法时
# 使用对象名字.属性名
# print(person.name)
# print(person.age)
# print(person.gender)

# 把person这个对象中的属性或行为进行修改
# person.name = 'lisi'
# print(person.name)
# person.age = 20
# print(person.age)
#
# person.height = 180
# print(person.height)
#
# del person.gender
# print(person.gender)

# 对方法（函数）的添加或修改
# def drink(self):
#     print('我要喝饮料')
#
# person.drink()
# # 需要导入一个库，来将新定义的函数与对象绑定起来
# from types import MethodType
# person.drink = MethodType(drink, person)
# person.drink()
#
# def say(self):
#     print('我会说话')
# person.say = MethodType(say, person)
# person.say()
#
# del person.say
# person.say()



# self参数
# class Person:
#     def say(self):
#         print(self)
#
# person1 = Person()
# person2 = Person()
# person1.say()
# print(person1)
# person2.say()
# print(person2)






# 构造函数与析构函数
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#         print('我被调用了')
#
#     def say(self):
#         print(f'我叫{self.name}，今年{self.age}岁了。')
#
# person1 = Person('zhangsan')
# person2 = Person('lisi', 20)
# print(person1.name)
# print(person2.name)
# person1.say()
# person2.say()


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('我是构造函数，我被调用了')
#
#     def __del__(self):
#         print('我是析构函数，我被调用了')
#
# person = Person('zhangsan', 18)




# 类中属性和方法的类别
# 1. 类属性：在类定义时所定义的属性，不和self绑定

# 如果类的所有的实例需要使用同一个数据时，就可以将该变量设置为类属性
# class Circle:
#     PI = 3.1415926
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         print(f'此圆的面积是{Circle.PI * self.radius * self.radius}')
#
# c1 = Circle(1)
# c2 = Circle(2)
# c1.area()
# c2.area()


# class BankCount:
#     total_amount = 0
#
#     def __init__(self, name, init_money):
#         self.name = name
#         BankCount.total_amount += init_money
#
#     def save_money(self, amount):
#         BankCount.total_amount += amount
#
#     def expend(self, amount):
#         BankCount.total_amount -= amount
#
# my_bank1 = BankCount('zhangsan', 10000)
# my_bank1.save_money(20000)
# my_bank1.expend(5000)
# print(BankCount.total_amount)
#
# my_bank2 = BankCount('lisi', 2000)
# print(BankCount.total_amount)



# 实例属性：属于对象的属性，和self参数绑定，且多在构造函数中定义
# class Person:
#     a = 1
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# person = Person('zhangsan', 18, 'nan')
#
#
# # __dict__:用来查看对象的属性，但是只能查看和self绑定了的属性
# print(person.__dict__)
# print(Person.__dict__)



# 实例方法：类中的函数，第一个参数是self的就是实例方法，就是对象调用的方法
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     def say(self):
#         print(f'我叫{self.name}')
#
# person = Person('zhangsan')
# person.say()
# person.change_name('lisi')
# person.say()




# class Circle:
#     def __init__(self, radius):
#         self.pi = 3.1415926
#         self.radius = radius
#
#     def area(self):
#         print(self.pi * self.radius * self.radius)
#
#     def lenth(self):
#         print(2 * self.pi * self.radius)
#
# c1 = Circle(1)
# c1.lenth()
# c1.area()









# 静态方法：有自己的参数，与类里的数据不共享，类和对象都可以调用
# 静态方法上面有一个标志：  @staticmethod

# class Calculator:
#
#     @staticmethod
#     def add(a, b):
#         print(a + b)
#
# Calculator.add(1, 2)
# cal = Calculator()
# cal.add(3, 4)





# 类方法：属于类本身的方法，用来访问和修改类属性，不能访问实例属性
class Person:
    name = 'zhangsan'

    @classmethod
    def change_name(cls, name):
        cls.name = name
        print(cls)

print(Person)
person = Person()
person.change_name('lisi')
print(person.name)

