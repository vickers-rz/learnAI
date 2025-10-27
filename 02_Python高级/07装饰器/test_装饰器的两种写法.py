def decorator(func):
    def inter(*args, **kwargs):
        print("参数装饰器开始执行")
        result = func(*args, **kwargs)
        print("参数装饰器结束执行")
        return result
    return inter


# @decorator # 用法一不用此语法糖
@decorator
def test(a, b):
    print(a, b)

# # 两种用法之一：
# final_func = decorator(test)
# final_func(1, 2)


# 两种用法之二：
test(1,2)

