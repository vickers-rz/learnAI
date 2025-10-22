'''
numbers = [15, 8, 23, 4, 42, 16]

# 初始化最大值和最小值
max_value = numbers[0]
min_value = numbers[0]

# 遍历列表来找到最大值和最小值
for number in numbers:
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

# 输出最大值和最小值
print("最大值:", max_value)
print("最小值:", min_value)
'''

numbers = [15, 8, 23, 4, 42, 16, 19, 20]
numbers[2:6] = 23, 11
numbers[2:5] = [22]

"""
numbers[2:3] = 12
TypeError: can only assign an iterable
而 12 是一个整数，不是一个可迭代对象。所以，当你尝试将一个单独的数字赋给切片时，Python 报错，
因为它期望一个可迭代对象（例如列表、元组、字符串等）来进行赋值。
如果你想用一个元组来赋值，需要在数字 12 前加上逗号，使其成为一个只有一个元素的元组
"""
numbers[2:4] = 12, #使用逗号来分隔值进行赋值时，实际上是将这些值作为一个元组传递给列表切片操作,
'''
同理：
numbers[2:3] = (24) 也会报同样的错
'''
numbers[2:3] = (24,) #
print(numbers)

