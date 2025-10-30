'''
5!  ===>非递归实现   5*4*3*2*1
     mul=1
     for i in range(n):
         mul*=i
    ===>递归实现为了简化操作
5!                           n!
  5*4!           120         n*(n-1)!
     4*3!         24       终止条件:(n==1)  return 1
        3*2!      6
          2*1!    2
          #终止条件
          1!=1     1
'''
def jiecheng(n):
     #终止条件
     if n==1:
         return 1

     return n*jiecheng(n-1)

print(jiecheng(5))