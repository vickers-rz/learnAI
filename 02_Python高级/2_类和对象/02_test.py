# 类的定义
class Person:
    name = 'zhangsan'
    age = 18
    gender = 'nan'

    def eat(self):
        print('我会吃饭')

    def drink(self):
        print('我会喝水')

# 创建对象
person = Person()
# 通过对象去调用类的属性和方法时
# 使用对象名字.属性名
person.eat()
person.drink()

print(person.name)
print(person.age)
print(person.gender)

# 把person这个对象中的属性或行为进行修改
person.name = 'lisi'
print(person.name)
person.age = 20
print(person.age)
#
print(person.gender)

'''
def drink(self):
    print('我要喝饮料')

person.drink()
# del person.gender
# print(person.gender)
如果取消注释并执行，会抛出错误：
AttributeError: 'Person' object has no attribute 'gender'
原因是：删除的是对象自己的属性，而对象本来没有单独的 gender 属性（只是继承自类），所以删除无效，之后访问时找不到该属性。
如果想真正替换 person 对象的 drink 方法，可以直接绑定函数给对象
'''
# 以下是解决方案：
"""
def drink2(self):
    print('我要喝饮料')
    
import types
person.drink = types.MethodType(drink2, person)
person.drink()  # 输出：我要喝饮料
"""



