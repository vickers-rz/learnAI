# f = open("1.txt","r")
# # str = f.readlines()
# # print(str)
# # print("=" * 40)
# str2 = f.read(2)
# print(str2)
# print("=" * 20)
# str3 = f.read(12)
# print(str3)
# print("=" * 20)
# str4 = f.read(22)
# print(str4)
# print("=" * 20)
# str5 = f.read(23)
# print(str5)
# print("=" * 20)
# f.close()
#
# f = open("1.txt","rb+")
# str = f.read()
# print(str)
with open("1.txt","rb") as fb:
    print(fb.read())


with open("1.txt","r") as fb:
    fb.readline()
    res = fb.tell()
    print(res)

    fb.readline()
    res = fb.tell()
    print(res)

    fb.readline()
    res = fb.tell()
    print(res)

    fb.readline()
    res = fb.tell()
    print(res)

    fb.readline()
    res = fb.tell()
    print(res)

    fb.readline()
    res = fb.tell()
    print(res)

    with open("1.txt", "r") as fb:
        line_number = 1
        previous_position = 0

        while True:
            # current_position = fb.tell()
            line = fb.readline()

            if not line:  # 文件结束
                break

            # 计算当前行的字符数（包括换行符）
            line_length = len(line)
            # 不包括换行符的字符数
            content_length = len(line.rstrip('\n'))

            print(f"第{line_number}行: {content_length}个字符 (含换行符共{line_length}个字符)")

            line_number += 1
