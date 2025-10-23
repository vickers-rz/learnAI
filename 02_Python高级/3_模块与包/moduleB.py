# 导入模块的第一种方法
import moduleA
#模块.函数名()
#模块.变量名

# 调用了模块A中的add函数
sumA = moduleA.add(2,3)
print(sumA)

# 调用模块A中的变量a
A = moduleA.a
print(A)

# 调用模块A里的类，创建对象

p1=moduleA.Person ('Wang',18)
# 调用对象方法: 对象名.方法名()
p1.show()

p2 = moduleA.Person('Zhang',18)
p2.show()

