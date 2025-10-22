# 关键字参数：使用 形参名字=实参 的方式传递，不用考虑形参的位置
# 关键字参数使用的场景很多
# sub(y = 2, x = 1)
# Python解释器规定位置参数必须在关键字参数之前传参
# 也就是说，当调用函数时，第一个传入的参数是关键字传参时，那么后面的参数就不能使用位置传参了
# sub(y=2, 1)
# help(sum)
# ls = [1, 2, 3]
# print('使用关键字传参：', sum(ls, start=1))
# print("使用位置参数传参：", sum(ls, 1))
# help(dict.fromkeys)
"""


"""
"""
不要把“可变对象”当作默认参数（如 [] / {}）；会“记住上次调用的修改”。
安全写法：默认值用 None，函数里再创建新对象。 解释以上
"""
"""
def add_item(item, bucket=[]): bucket.append(item); return bucket

print(add_item(1))
print(add_item(2))

def add_item(item, bucket=None):
    if bucket is None: bucket = []
    bucket.append(item);
    return bucket

print(add_item(1))
print(add_item(2))
"""

"""
# 默认参数(也就是kwargs) 默认在定义时，必须放在形参的最右边

def add(x, y = 2, z = 1):
    print('x的值为：', x)
    print('y的值为：', y)
    print('z的值为：', z)

print(add(1))
'''
print(add(1,,3))
# 语法错误。不能用空逗号跳过 `y`。想改 `z` 可写 `add(1, z=3)`；想改 `y` 写 `add(1, 3)`。
'''
print(add(1,2,3))
# 如果需要修改默认参数的值，可以传递实参来覆盖掉默认参数的默认值
print(add(1, y=3, z = 5))
# 默认参数在调用函数时如果不需要修改默认参数的值就可以不传递
# add(1, y=3, z = 5)
"""

# 函数的多个返回值
'''
def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组-可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 如果函数返回的类型是元组，小括号可以省略
    # return (temp, wetness)
    return temp, wetness

# 元组
result = measure()
print(result)

# 需要单独的处理温度或者湿度 - 不方便
print(result[0])
print(result[1])

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元组中元素的个数保持一致
gl_temp, gl_wetness = measure() # 此处绝妙！

print(gl_temp)
print(gl_wetness)
'''

"""
# 对传入的关键字参数的值进行相乘
def mul(**kwargs):
    result = 1
    # 使用kwargs.keys()获取字典中所有的键
    # 通过for循环取遍历这些键，从而获取对应的值并令该值参与运算
    for key in kwargs.keys():
        result = kwargs[key] * result
    print(result)

# mul(a = 1, b = 2, c = 3)
"""


"""
def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)

# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)
"""
"""
区分位置参数、*args 和 **kwargs 的方式：
位置参数：这些参数直接按顺序传递，必须位于所有的 *args 和 **kwargs 之前。
*args：收集所有 额外的 位置参数（位置参数在 *args 前面传递）。*args 将这些位置参数打包成一个元组。
**kwargs：收集所有 关键字参数。关键字参数是通过 key=value 形式传递的，它们将被打包成一个字典，并且只能出现在参数列表的最后。

函数调用时的实参顺序：
位置参数：传递的第一个位置参数会匹配到定义中的第一个参数。
*args：之后的所有额外位置参数会被打包成一个元组传递给 *args。

**kwargs：最后的 关键字参数 会被打包成字典，传递给 **kwargs
"""

"""
def test1(*args, x, y):
    print(args)
    print(x)
    print(y)

test1(1, 2, 3, x=4, y=5)
# 或 test1(1, 2, 3, y=5, x=4) # 都是一样的结果

# 运行结果：
```
(1, 2, 3)  # args
4          # x
5          # y
```
在你的代码中：
* `*args` 允许接收 **任意数量的** 位置参数，传递给 `args`。
* 代码中，`x` 和 `y` 的位置确实会让人困惑，然而它是合法的。`x` 和 `y` 其实是 **关键字参数**，而非位置参数。它们必须通过 **关键字传递**，即通过 `x=4` 和 `y=5` 进行传递。
"""


def div(x, y):
    if y == 0:
        pass
    else:
        return x / y
    return '除数不能为0'
print(div(1, 0))