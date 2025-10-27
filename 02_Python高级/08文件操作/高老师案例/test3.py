# 每隔5秒将系统时间写入到文件中
# 格式为：行数,系统时间
'''
   <1>.以追加的方式打开文件"a+"  open()
   <2>.将文件光标移动到文件开头  f.seek()
   <3>.为了获取该文件有多少行  写一个子函数,实现文件的行数 f.readline()   line
   while True:
   <4>.获得系统时间,
   <5>.将行数,系统时间写入到文件中
   <6>.每隔开5秒 time.sleep(5)
'''
# while True:
# time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# time.sleep(5)

import  time
# 为了获取该文件有多少行  写一个子函数,实现文件的行数
def get_line_count(file_path):
    '''统计文件行数'''
    count = 0
    with open(file_path, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            count += 1
    return count


file_path = "time.log"
while True:

    # 获取当前文件已有的行数
    line_num = get_line_count(file_path) + 1

    # 获取当前系统时间
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        # 以追加方式写入文件
        with open(file_path, "a+", encoding="utf-8") as f:
            f.write(f"{line_num},{time_now}\n")

        print(f"写入第{line_num}行：{time_now}")
        time.sleep(5)

    except KeyboardInterrupt:
        print("\n手动中断程序，文件已保存。")
        break
    except Exception as e:
        print(f"错误：{e}")
        break

