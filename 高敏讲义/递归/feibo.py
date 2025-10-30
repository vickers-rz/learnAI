#0 1 1 2 3 5 8 13 21
#第一个数为0  第二个数1  从第三个数开始为前两项之和

#递归
#第n项的值为第n-1项的值+n-2项的值
def feibo(n):
    #终止条件
    if n==1:
        return 0
    elif n==2:
        return 1
    
    return feibo(n-1)+feibo(n-2)

list=[]
for i in range(1,11):
    list.append(feibo(i))
print(list)