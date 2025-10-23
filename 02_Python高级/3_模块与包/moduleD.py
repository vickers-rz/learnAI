# 只导入模块a的变量
from moduleA import a
print(a)
# 只导入模块a的函数
from moduleA import add
print(add(2,5))
# 只导入模块a的类
from moduleA import Person as ps
p1=ps('zhangsan',28)
p1.show()


from moduleA  import * #当使用 from module import * 时，Python 解释器会自动将源模块中所写到的 __all__ 中的对象导入到当前作用域

print(a)
print(add(2,5))
print(sub(1,2))
print(mul(2,5))
# print(div(10,2)) # 会报错：模块a中没有div函数，因为 __all__ 中没有div

import moduleA
print(add(2,5))
print(moduleA.div(10,2))
print(moduleA.mul(2,5))

