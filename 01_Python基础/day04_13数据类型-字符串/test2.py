"""
解一元二次方程 ax^2 + bx + c = 0 的根，要求如下：
1. 用户输入三个系数 a, b, c，且 a ≠ 0。
2. 使用判别式（delta）来判断方程的根：
   - 如果 delta > 0，方程有两个不同的实数根。
   - 如果 delta = 0，方程有一个重复的实数根。
   - 如果 delta < 0，方程没有实数根。
3. 使用 math.sqrt() 计算判别式的平方根，不使用其他辅助函数。
"""

import math

# 获取用户输入的 a, b, c
while True:
    a = float(input("请输入a:"))
    if a == 0:
        print("a 不能为 0，请重新输入 a ≠ 0 的值。")
    else:
        break  # 如果 a != 0，则退出循环
b = float(input("请输入b:"))
c = float(input("请输入c:"))


 # 计算判别式
delta = b * b - 4 * a * c
if delta < 0:
    print("没有实数根")
elif delta > 0:
    # 使用 math.sqrt 计算平方根
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"delta > 0：两个不相等的实数根:x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"delta = 0：两个相等的实数根:x = {x}")


