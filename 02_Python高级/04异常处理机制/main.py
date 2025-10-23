# -*- coding: utf-8 -*-
# KeyboardInterrupt：用户主动结束程序去触发的
"""
import time
for i in range(100):
    print(i)
    time.sleep(1)
"""

"""
# AttributeError:尝试访问对象所没有的属性时触发
my_str = 'abcdef'
#my_str.abc()
#print(my_str.islower())
"""

# # IndexError:访问不存在的索引时会触发
# my_list = [1, 2, 3]
# print(my_list[10])


# 捕获单个异常
"""
try:
    x = 10
    y = 0
    print(x / y)
except ZeroDivisionError:
    print('除数不能为0')
"""

# 捕获多个异常
# try:
#     print(a)
#     x = 10
#     y = 1
#     z = x / y
# except (ZeroDivisionError, NameError):
#     print('除数不能为0')
# else:
#     print(z)

"""
try:
    x = 10
    y = 2
    print(x / y + z)
except (ZeroDivisionError):
    print('除数不能为0')
except NameError:
    print('没有定义变量z')
else:
    print("运行正常")
finally:
    print('程序已退出')
"""


"""
try:
    x = 10
    y = 2
    z = 1
    print(x / y + z)
except (ZeroDivisionError, NameError):
    print('除数不能为0，或没有定义变量z')
else:
    print("运行正常")
finally:
    print('程序已退出')
"""

# 捕获所有的异常
# try:
#     print(a)
#     x = 10
#     y = 0
#     z = x / y
# except Exception as e:
#     print(e)


"""
try:
    x = 10
    y = 0
    z = 0
    print(x / y + z)
except Exception as e:
    print(e)
else:
    print("运行正常")
finally:
    print('程序已退出')
"""
# 手动抛出异常1
"""
x = 10
y = 0
if y == 0:
    raise ZeroDivisionError('除数不能为0')
"""
# 创建自己的异常类
'''
class MyException(Exception):
    def __init__(self,message,ErrCode=None,traceback=None):
        super().__init__(message)
        self.ErrCode = ErrCode
        self.traceback = traceback

raise MyException('手动抛出的',102)
'''



# 在Python里，记录日志使用logging库，日志的级别从高到底分别为：
# 1.CRITICAL:系统崩溃级别的错误，必须立即处理
# 2.ERROR：运行时的错误，可能导致程序无法正常执行
# 3.WARNING:警告信息
# 4.INFO：信息性消息，程序正常运行
# 5.DEBUG：详细信息，通常在诊断问题时有用

"""
import logging
logging.basicConfig(level=logging.CRITICAL)
logging.critical('这是一个严重错误')
logging.error('这是一个错误信息')
logging.warning('这是一个警告信息')
logging.info('这是一个信息')
logging.debug('这是一个调试信息')
"""
# # 向指定的日志文件里去打印日志信息
# import logging
# logging.basicConfig(filename='./app.log', level=logging.DEBUG, filemode='a', format='%(name)s - %(levelname)s - %(asctime)s- %(message)s')
# logging.warning('这是一个警告信息')
#
# # %(name)s:日志记录器的名字
# # %(levelname)s:日志级别
# # %(asctime)s: 时间
# # %(message)s: 消息本身
import logging
logger1 = logging.getLogger("wangwu")
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger1.critical('这是一个严重错误')



# # 创建自己的日志处理器
# import logging
# logger = logging.getLogger('mylogger')
# logging.basicConfig(filename='./app.log', level=logging.DEBUG, filemode='a', format='%(name)s - %(levelname)s - %(asctime)s- %(message)s')
# logger.warning('这是我自己定义的日志处理器所记录的日志')
