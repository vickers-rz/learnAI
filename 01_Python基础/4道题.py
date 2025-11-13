### 4-1. 生成斐波那契数列
'''
每个数字是前两个数字的和
1, 1, 2, 3, 5, 8, 13, 21, 34
给定一个数字，生成前面的n项
'''
"""
n = int(input("给定一个数字，生成前面的n项:"))
feibo = [1, 1]
for i in range(2, n):
    next_num = feibo[-1] + feibo[-2]
    feibo.append(next_num)
print(str(feibo).strip("[]"))
"""

### 4-2. 判断一个数字是否为素数
"""
* 素数定义：大于1的自然数，除了1和其自身外，不能被任何其它整数整除。
输入：一个整数`num` , 输出：返回该数字是否为素数。
* 优化点：使用`sqrt(num)`来减少计算的次数，因为一个数的因数只会出现在它的平方根以内。
* 判断条件：`num`从2到`sqrt(num)`逐一检查是否能整除。
1. **定义函数**，接收一个整数`num`。
2. 先排除小于2的数字（直接返回`False`）。
3. 判断从2到`sqrt(num)`范围内是否有数能整除`num`。
4. 如果有则返回`False`，否则返回`True`。
"""


import math
num = int(input("输入一个整数:"))
if num <= 1:
    print("不是素数")
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        print("不是素数")
    else:
        print("是素数")


