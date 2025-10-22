'''
# 案例1
x = 10

match x:
    case 10:
        print("x的值为10.")
    case 20:
        print("x的值为20.")
    case _:
        print("x的值既不是10也不是20")
'''

'''
# 案例2
x = 2
match x:
    case 1 | 2 | 3:
        print("x的值为1、2、3中的一个")
    case _:
        print("x的值不是1、2、3")
'''


# 案例3
x = 10
match x:
    case x if x > 5:
        print("x的值比5大")


