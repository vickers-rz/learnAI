def fib(n):
    """生成斐波那契数列，直到第 n 个数字（使用中间变量）"""
    fib_list = []
    a, b = 0, 1
    while len(fib_list) < n:
        fib_list.append(a)
        temp = a + b  # 计算下一项
        a = b         # 当前项向前推进
        b = temp      # 更新下一项
    return fib_list

print(f'中间变量方式：{fib(10)}')

