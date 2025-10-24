def decorator(func):
    def inner():
        print("在原函数执行前做的事情")
        result = func()  # 执行原函数
        print("在原函数执行后做的事情")
        return result
    return inner


def hello():
    print("Hello, World!")

hello = decorator(hello)
hello()

'''
装饰器执行细节拆解：

1. 定义decorator函数：
   - 接受一个函数func作为参数
   - 在内部定义inner函数，用于包装原函数
   - inner函数中先打印前置信息，然后调用func()，再打印后置信息
   - 最后返回inner函数对象（注意不是执行结果）

2. 定义hello函数：
   - 这是一个简单的函数，只打印"Hello, World!"

3. 装饰过程：hello = decorator(hello)
   - 将hello函数作为参数传递给decorator函数
   - decorator函数内部创建inner函数，该函数引用了hello函数
   - decorator返回inner函数对象，并将其赋值给hello变量
   - 此时hello变量不再指向原来的hello函数，而是指向inner函数

4. 执行过程：hello()
   - 调用的是inner函数（因为hello现在指向inner函数）
   - inner函数首先打印"在原函数执行前做的事情"
   - 然后调用原来的hello函数（通过闭包机制保存的func）
   - 原来的hello函数执行，打印"Hello, World!"
   - inner函数继续执行，打印"在原函数执行后做的事情"
   - 返回原函数的执行结果（这里为None）

这就是装饰器的工作原理：
- 通过高阶函数（接受函数作为参数并返回函数）实现
- 利用闭包机制保存原函数的引用
- 在不修改原函数代码的情况下扩展其功能
'''