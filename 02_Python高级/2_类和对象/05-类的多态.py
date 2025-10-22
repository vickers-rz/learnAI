
# str1 = 'abcdef'
# ls1 = [1, 2, 3, 4, 5]
# tp1 = (1, 2, 3)
# dic ={1: 1, 2: 2, 3: 3, 4: 4}
# print(len(str1))
# print(len(ls1))
# print(len(tp1))
# print(len(dic))




# 鸭子模型：我想要一只鸭子，我没有鸭子，但是我有一只鸡，但是这只鸡走路像鸭子，叫声也向鸭子
# 这只鸡拥有鸭子的功能，那么我就认为这只鸡就是鸭子

class Cat:
    def say(self):
        print('miao~~~~')


class Dog:
    def say(self):
        print('wang~~~~')

class Sheep:
    def say(self):
        print('mie~~~~')

def call(x):
    x.say()


cat = Cat()
dog = Dog()
sheep = Sheep()


call(cat)
call(dog)
call(sheep)


class Plane:
    def say(self):
        print('我会飞')

plane = Plane()
call(plane)