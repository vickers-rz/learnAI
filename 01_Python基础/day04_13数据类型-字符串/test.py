"""
# 循环控制关键字的用法

# break  continue  pass
i = 1

while i <= 5:
    if i == 3:
        i += 1
        pass
    print(i)
    i += 1
"""
'''
编写一个 Python 脚本，接收用户输入的身高（单位：米）和体重（单位：公斤）。
计算并打印身体质量指数（BMI）。BMI 计算公式为：
BMI = 体重 / （身高 * 身高）
根据 BMI 值打印出对应的健康状况：
BMI < 18.5: 过轻
18.5 <= BMI < 24: 正常
24 <= BMI < 28: 过重
BMI >= 28: 肥胖
'''
'''
# 获取用户输入的身高（单位：m）和体重（单位：kg）
height = float(input("输入身高（m）："))
weight = float(input("输入体重(kg):"))
# 计算 BMI
BMI = weight / (height ** 2)

# 打印 BMI 值，判断并输出健康状况
print(BMI)
if BMI < 18.5:
    print("过轻")
elif 18.5 <= BMI < 24:
    print("正常")
elif 24 <= BMI < 28:
    print("过重")
elif 28 <= BMI:
    print("肥胖")
'''

'''
解一元二次方程 ax^2 + bx + c = 0 的根，要求如下：
1. 用户输入三个系数 a, b, c，且 a ≠ 0。
2. 使用判别式（delta）来判断方程的根：
   - 如果 delta > 0，方程有两个不同的实数根。
   - 如果 delta = 0，方程有一个重复的实数根。
   - 如果 delta < 0，方程没有实数根。
3. 使用 math.sqrt() 计算判别式的平方根，不使用其他辅助函数。
'''

import math

# 获取用户输入的 a, b, c
print("请输入 a, b, c（以空格分隔，且 a ≠ 0）：")
a_str = input("a = ")
b_str = input("b = ")
c_str = input("c = ")

# 将输入的字符串转换为浮点数
a = float(a_str)
b = float(b_str)
c = float(c_str)

# 如果 a 为 0，返回错误
if a == 0:
    print("a 不能为 0")
else:
    # 计算判别式（简化判断）
    delta = b * b - 4 * a * c

    # 使用 math.sqrt 直接计算平方根
    if delta > 0:
        sqrt_delta = math.sqrt(delta)  # 计算正的判别式的平方根

        # 两个不同的实数根
        x1 = (-b - sqrt_delta) / (2 * a)
        x2 = (-b + sqrt_delta) / (2 * a)
        print("delta > 0：两个不相等的实数根")
        print(f"x1 = {x1}, x2 = {x2}")

    # 判别式 delta = 0
    elif delta == 0:
        # 单一的实数根
        x = -b / (2 * a)
        print("delta = 0：两个相等的实数根")
        print(f"x = {x}")


