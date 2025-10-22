#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python面向对象编程 - 多态（Polymorphism）示例代码

多态是面向对象编程的三大特性之一（封装、继承、多态）
多态指的是同一个接口可以有不同的实现方式
"""

# 1. 基础多态示例
# ================================

class Animal:
    """动物基类"""
    def __init__(self, name):
        self.name = name  # 动物的名字
    
    def speak(self):
        """
        发出声音的方法 - 这是一个抽象方法
        子类必须重写这个方法
        """
        pass  # 基类中不实现具体功能


class Dog(Animal):
    """狗类，继承自Animal"""
    
    def speak(self):
        """
        重写父类的speak方法
        实现狗的叫声
        """
        return f"{self.name} says: 汪汪!"


class Cat(Animal):
    """猫类，继承自Animal"""
    
    def speak(self):
        """
        重写父类的speak方法
        实现猫的叫声
        """
        return f"{self.name} says: 喵喵!"


class Duck(Animal):
    """鸭子类，继承自Animal"""
    
    def speak(self):
        """
        重写父类的speak方法
        实现鸭子的叫声
        """
        return f"{self.name} says: 嘎嘎!"


# 演示多态的使用, 创建不同动物的实例
dog = Dog("小白")
cat = Cat("小花")
duck = Duck("小黄")

# 将所有动物放入列表中
animals = [dog, cat, duck]

# 遍历动物列表，调用speak方法
# 虽然调用的都是speak()方法，但由于对象类型不同，实际执行的是各自类中的speak方法
for animal in animals:
    # 这里体现了多态：同一个方法调用，有不同的行为表现
    print(animal.speak())


# 2. 多态与函数参数
# ================================

def animal_speak(animal):
    """
    接受Animal类型或其子类的函数
    这个函数展示了多态在函数参数中的应用
    
    参数:
        animal (Animal): Animal类或其子类的实例
    """
    # 不管传入的是Dog、Cat还是Duck实例，都会调用对应类的speak方法
    return animal.speak()


print("\n=== 多态与函数参数 ===")
# 使用同一个函数处理不同类型的动物对象
print(animal_speak(dog))   # 调用Dog类的speak方法
print(animal_speak(cat))   # 调用Cat类的speak方法
print(animal_speak(duck))  # 调用Duck类的speak方法


# 3. 更复杂的多态示例 - 形状计算
# ================================

class Shape:
    """形状基类"""
    
    def area(self):
        """
        计算面积的方法 - 抽象方法
        子类必须实现
        """
        pass
    
    def perimeter(self):
        """
        计算周长的方法 - 抽象方法
        子类必须实现
        """
        pass


class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width, height):
        """
        初始化矩形
        
        参数:
            width (float): 矩形的宽度
            height (float): 矩形的高度
        """
        self.width = width
        self.height = height
    
    def area(self):
        """计算矩形面积"""
        return self.width * self.height
    
    def perimeter(self):
        """计算矩形周长"""
        return 2 * (self.width + self.height)


class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius):
        """
        初始化圆形
        
        参数:
            radius (float): 圆的半径
        """
        self.radius = radius
    
    def area(self):
        """计算圆形面积"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """计算圆形周长（ circumference）"""
        return 2 * 3.14159 * self.radius


class Triangle(Shape):
    """三角形类"""
    
    def __init__(self, a, b, c):
        """
        初始化三角形
        
        参数:
            a, b, c (float): 三角形的三条边长
        """
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        """
        使用海伦公式计算三角形面积
        """
        # 半周长
        s = (self.a + self.b + self.c) / 2
        # 海伦公式
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        """计算三角形周长"""
        return self.a + self.b + self.c


print("\n=== 形状计算多态示例 ===")
# 创建不同形状的实例
rectangle = Rectangle(5, 3)
circle = Circle(4)
triangle = Triangle(3, 4, 5)

# 将所有形状放入列表
shapes = [rectangle, circle, triangle]

# 遍历所有形状，计算面积和周长
# 同样的方法调用，不同的实现方式
for shape in shapes:
    print(f"{type(shape).__name__}:")
    print(f"  面积: {shape.area():.2f}")
    print(f"  周长: {shape.perimeter():.2f}")


# 4. 使用isinstance检查对象类型
# ================================

print("\n=== 类型检查 ===")
for shape in shapes:
    # isinstance()函数用于检查对象是否是某个类或其子类的实例
    if isinstance(shape, Rectangle):
        print(f"{shape} 是矩形")
    elif isinstance(shape, Circle):
        print(f"{shape} 是圆形")
    elif isinstance(shape, Triangle):
        print(f"{shape} 是三角形")
    else:
        print(f"{shape} 是未知形状")


# 5. 抽象基类（更严格的多态）
# ================================

from abc import ABC, abstractmethod

class AbstractShape(ABC):
    """
    抽象形状基类
    使用ABC（Abstract Base Class）创建更严格的抽象类
    """
    
    @abstractmethod
    def area(self):
        """抽象方法：计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """抽象方法：计算周长"""
        pass


class Square(AbstractShape):
    """正方形类"""
    
    def __init__(self, side):
        """
        初始化正方形
        
        参数:
            side (float): 正方形的边长
        """
        self.side = side
    
    def area(self):
        """计算正方形面积"""
        return self.side ** 2
    
    def perimeter(self):
        """计算正方形周长"""
        return 4 * self.side


print("\n=== 抽象基类示例 ===")
# 创建正方形实例
square = Square(4)

print(f"正方形:")
print(f"  面积: {square.area()}")
print(f"  周长: {square.perimeter()}")

# 抽象基类不能被直接实例化
# 下面这行代码会报错：
# abstract_shape = AbstractShape()  # TypeError: Can't instantiate abstract class

print("\n=== 多态的优势 ===")
print("1. 代码可扩展性好：添加新的形状类不需要修改现有代码")
print("2. 代码复用性高：可以使用统一的接口处理不同的对象")
print("3. 降低耦合度：调用者不需要关心具体是哪种类型的对象")
print("4. 提高可维护性：每个类负责自己的实现，职责清晰")