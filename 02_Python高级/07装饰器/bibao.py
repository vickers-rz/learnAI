# # 闭包函数的原理
# def  nth_power(exponent):  #exponent=2
#     def exponent_of(base):  # base=5
#         return base ** exponent   # 5**2
#     return exponent_of
#
#
# square=nth_power(2)   # exponent=2
# #print(square(2))
# print(square(5))  #base=5
#
#
# cube=nth_power(3)  #exponent=3
# print(cube(5))  #base=5


# 闭包 + nonlocal
# 1 有嵌套
def func_out(num1):
    def func_in(num2):
        nonlocal num1 # 没有nonlocal，会报错,就会没有权限去修改外层函数中的变量num1。
        # 2 有引用
        num1 = num1 + num2
        print('num1-->', num1)
    # 3 有返回
    return func_in

myf = func_out(10)
myf(1)
myf(1)
myf(1)

# 定义一个闭包函数，求解y = ax + b
def func(a, b):
    def func_in(x):
        return a * x + b
    return func_in
func_out = func(2, 1)
print(func_out(5))
print(func_out(10))
