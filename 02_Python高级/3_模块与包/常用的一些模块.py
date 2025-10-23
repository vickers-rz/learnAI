"""
模块名称 模块描述
os与sys  关于与系统交互的模块，比如文件夹的创建与修改。
math    数学库，里面提供了关于数学的函数，比如三角函数。
time    time模块提供了时间相关的函数，例如获取当前时间。
random  用于生成随机数的模块。
threading   线程库，用于提供多线程多需要的接口。
"""

'''
# # os模块
import os

from nbclient.client import timestamp

dir_name = 'new_folder/new_dir'
print('当前目录:', os.getcwd())
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f'{dir_name}已创建成功！！！')
else:
    print('该文件夹已存在！！')

# # sys模块
import sys

# 使用sys模块打印Python解释器版本
print(f'该文件使用的Python解释器的版本为：', sys.version)

"""
# 终止程序
# sys.exit(0)
# exit()
"""
print('123')

'''

# math模块
# import math
# print(math.pi)
#
# a = math.pi
# print(math.sin(a))


# # time模块
import time
# start = time.time()
# time.sleep(1)
# stop = time.time()
# print(stop - start)

"""
timestamp = time.time()
# print(timestamp)
# print(time.localtime(timestamp))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print(time.mktime(time.strptime("2023-03-20 22:24:24", "%Y-%m-%d %H:%M:%S")))
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime()))
print(time.strftime("%Y年%m月%d日 %A", time.localtime()))
# 修改AM/PM显示为上午/下午
time_str = time.strftime("%Y年%m月%d日 %I:%M:%S %p", time.localtime())
time_str_chinese = time_str.replace('AM', '上午').replace('PM', '下午')
print(time_str_chinese)
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))
"""
# random模块
import random
# a = random.randint(1, 10)
# print(a)


my_list = [1, 2, 3, 4, 5]
# 将列表中的元素随机打乱
random.shuffle(my_list)
print(my_list)