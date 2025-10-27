#
#
#
# #withy语句经常使用，open文件给对象f,自动关闭文件
# with open("1.txt","r") as f:
#     str=f.readlines()
#     print(str)


# import time
#
#
# def RecTime():
#     """返回一个闭包函数，用于记录时间日志"""
#     number = 0  # 用于记录行号
#
#     def inner():
#         nonlocal number
#         with open("time.log", "a+", encoding="utf-8") as f:
#             while True:
#                 number += 1
#                 time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#                 f.write(f"{number},{time_now}\n")
#                 f.flush()
#                 print(f"第 {number} 行已写入：{time_now}")
#                 time.sleep(5)
#
#     return inner
#
#
# # 创建闭包并执行
# recorder = RecTime()
# recorder()
