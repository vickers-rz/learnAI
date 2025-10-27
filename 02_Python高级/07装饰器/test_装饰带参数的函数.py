def parameter_dct(flag):
    def decorator(func):
        def inter(*args, **kwargs):
            if flag == "+":
                print("正在进行加法计算")
            else:
                print("正在进行减法计算")
            func(*args, **kwargs)
        return inter
    return decorator

@parameter_dct("+")
def add(a, b):
    result = a + b
    print(result)

@parameter_dct("-")
def sub(a, b):
    result = a - b
    print(result)


add(1, 2)
sub(3, 4)



