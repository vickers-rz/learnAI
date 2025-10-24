"""
Python装饰器详解

装饰器（Decorator）是Python的一个强大特性，它允许我们在不修改原函数代码的情况下，
给函数增加新的功能。装饰器本质上是一个接受函数作为参数并返回函数的高阶函数。
"""

# 一、最简单的装饰器示例
print("=" * 50)
print("一、最简单的装饰器示例")
print("=" * 50)


def simple_decorator(func):
    """
    最简单的装饰器
    :param func: 被装饰的函数
    :return: 新的函数
    """
    def wrapper():
        print("在原函数执行前做的事情")
        func()  # 执行原函数
        print("在原函数执行后做的事情")
    return wrapper


def hello():
    """原始函数"""
    print("Hello, World!")


# 使用装饰器的方式1：手动调用
print("1. 手动使用装饰器:")
decorated_hello = simple_decorator(hello)
decorated_hello()

print("\n" + "-" * 30 + "\n")

# 使用装饰器的方式2：使用@语法糖
print("2. 使用@语法糖:")


@simple_decorator
def goodbye():
    """使用@语法糖装饰的函数"""
    print("Goodbye, World!")


goodbye()

# 二、带参数的函数装饰器
print("\n" + "=" * 50)
print("二、带参数的函数装饰器")
print("=" * 50)


def arg_decorator(func):
    """
    可以处理带参数函数的装饰器
    使用*args和**kwargs可以接收任意参数
    """
    def wrapper(*args, **kwargs):
        print(f"函数 {func.__name__} 被调用，参数为: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)  # 执行原函数并获取结果
        print(f"函数 {func.__name__} 执行完毕")
        return result
    return wrapper


@arg_decorator
def greet(name, greeting="Hello"):
    """
    带参数的函数
    :param name: 名字
    :param greeting: 问候语
    :return: 问候字符串
    """
    message = f"{greeting}, {name}!"
    print(message)
    return message


# 调用带参数的装饰函数
print("调用带参数的装饰函数:")
result = greet("张三", greeting="你好")
print(f"函数返回值: {result}")

# 三、带参数的装饰器
print("\n" + "=" * 50)
print("三、带参数的装饰器")
print("=" * 50)


def repeat(times):
    """
    带参数的装饰器工厂函数
    :param times: 重复次数
    :return: 真正的装饰器函数
    """
    def decorator(func):
        """
        实际的装饰器函数
        :param func: 被装饰的函数
        :return: 包装后的函数
        """
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"第{i+1}次调用函数 {func.__name__}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


@repeat(3)
def say_hello(name):
    """
    简单的打招呼函数
    :param name: 名字
    :return: 打招呼的字符串
    """
    message = f"Hello, {name}!"
    print(message)
    return message


print("使用带参数的装饰器:")
results = say_hello("李四")
print(f"所有调用的结果: {results}")

# 四、类装饰器
print("\n" + "=" * 50)
print("四、类装饰器")
print("=" * 50)


class CountCalls:
    """
    类装饰器：统计函数被调用的次数
    """
    def __init__(self, func):
        """
        初始化装饰器
        :param func: 被装饰的函数
        """
        self.func = func
        self.count = 0  # 计数器

    def __call__(self, *args, **kwargs):
        """
        使类实例可以像函数一样被调用
        """
        self.count += 1
        print(f"函数 {self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)


@CountCalls
def fibonacci(n):
    """
    计算斐波那契数列的第n项（简单实现）
    :param n: 项数
    :return: 第n项的值
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print("使用类装饰器统计函数调用次数:")
print(f"fibonacci(5) = {fibonacci(5)}")

# 五、多个装饰器的使用
print("\n" + "=" * 50)
print("五、多个装饰器的使用")
print("=" * 50)


def bold_decorator(func):
    """
    给文本加粗的装饰器
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper


def italic_decorator(func):
    """
    给文本斜体的装饰器
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper


# 注意装饰器的应用顺序：从下往上应用
@bold_decorator
@italic_decorator
def get_text(text):
    """
    获取文本
    :param text: 输入文本
    :return: 文本
    """
    return text


print("使用多个装饰器:")
text = get_text("这是一个测试文本")
print(f"装饰后的文本: {text}")
print("注意：装饰器的应用顺序是从最靠近函数定义的开始，依次向上应用")

# 六、实用装饰器示例：计时器
print("\n" + "=" * 50)
print("六、实用装饰器示例：计时器")
print("=" * 50)


import time


def timer(func):
    """
    计时装饰器：计算函数执行时间
    :param func: 被装饰的函数
    :return: 包装后的函数
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 执行原函数
        end_time = time.time()  # 记录结束时间
        elapsed_time = end_time - start_time  # 计算耗时
        print(f"函数 {func.__name__} 执行耗时: {elapsed_time:.6f} 秒")
        return result
    return wrapper


@timer
def slow_function(seconds):
    """
    模拟耗时操作
    :param seconds: 睡眠秒数
    """
    time.sleep(seconds)
    return f"完成了 {seconds} 秒的操作"


print("使用计时装饰器:")
result = slow_function(1)
print(f"函数返回值: {result}")

print("\n" + "=" * 50)
print("装饰器学习总结")
print("=" * 50)
print("""
装饰器的核心要点：

1. 装饰器本质是一个函数，它接受一个函数作为参数，并返回一个新的函数
2. 使用@语法糖可以更方便地应用装饰器
3. 为了能处理任何参数类型的函数，装饰器内部通常使用*args和**kwargs
4. 带参数的装饰器实际上是一个返回装饰器的函数（装饰器工厂）
5. 类也可以作为装饰器，需要实现__call__方法
6. 多个装饰器会按照从下往上的顺序依次应用
7. 装饰器在函数定义时就会被应用，而不是在函数调用时

装饰器的常见应用场景：
- 日志记录
- 性能测试
- 权限校验
- 缓存机制
- 事务处理
""")