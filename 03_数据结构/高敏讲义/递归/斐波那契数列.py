
#循环方式

def fib(n):
    """生成斐波那列数列,直到第n个数字"""
    fib_list=[]
    a,b = 0,1
    while len(fib_list)<n:
        fib_list.append(a) #[0,1]
        a,b = b,a+b
    return fib_list

print("循环方式:",fib(10))


#递归方式
def  fib(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_list=fib(n-1)   #n=4   [0,1,1]
        #print(fib_list)
        fib_list.append(fib_list[-1]+fib_list[-2]) #[0,1,1,2]
        return fib_list

print("递归:",fib(1))
print("递归:",fib(2))
print("递归:",fib(3))
print("递归:",fib(4))