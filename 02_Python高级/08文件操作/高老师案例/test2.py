# with open("1.txt","r+") as fd :
#     res = fd.tell()
#     print(res)
#     print(fd.read())
#     print("=" * 30)
#     fd.seek(5)
#     ret = fd.read()
#     print(ret)

with open("3.txt","rb+") as fd2:
    res = fd2.tell()
    print(res)
    fd2.seek(-5,2)
    res = fd2.tell()
    print(fd2.read())
    print(res)