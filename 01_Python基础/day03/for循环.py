
'''
# for循环的简单使用

my_list = [1, 2, 3, 4, 5]

i = 1
for i in my_list:
    print(i)

print(i)

'''


# range()函数的用法
# range(start, stop, step)

# i = 1
# while i <= 5:
'''
for i in range(5):
    print(i)
'''

'''
# len()函数的用法
name = 'zhangsan'
print(len(name))

my_list = [1, 2, 3, 4]
print(len(my_list))
'''
'''
# 案例1  1-100求和
# 定义一个变量，用来接收求和的结果
sum = 0
# 0, 1, 2, 3, 4
for i in range(5):
    sum += i
print(sum)

'''

'''

# 案例2 输出100-999范围内的所有的水仙花数
# 水仙花数就是 个位的三次方 + 十位的三次方 + 百位的三次方 == 数本身

# 个位数
g = 0
# 十位数
s = 0
# 百位数
b = 0


for i in range(100, 1000):
    # i = 100
    # 通过i对10进行取余，可以得到个位数的值
    g = i % 10

    # 通过i对10进行取整，得到前两位数，然后通过前两位数对10进行取余，得到十位数的值
    s = i // 10 % 10

    # 通过i对100进行取整，可以得到百位数的值
    b = i // 100

    # 判断个位数的三次方+十位数的三次方+百位数的三次方是否等于数本身
    if g * g * g + s * s * s + b * b * b == i:
        print(f"{i}是一个水仙花数")
'''


# 案例3  使用for 循环完成99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {j * i}', end=' ')
    print()



