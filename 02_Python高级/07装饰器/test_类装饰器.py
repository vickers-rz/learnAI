class CountCalls:
    """
    类装饰器：统计函数被调的次数
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
        self.count += 1  # 增加调用计数
        return self.func(*args, **kwargs)  # 执行原函数并返回结果

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
print(f"fibonacci(3) = {fibonacci(3)}")
