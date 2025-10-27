

f=open("1.txt","r")
f.seek(0,2)      #移动文件光标的位置  #0 从文件开头移动  1 从文件当前位置移动  2.从文件末尾移动
filesize=f.tell() #tell()获得文件光标的位置
print("filesize=",filesize)


#<1>.f=open("文件名"，"打开方式",encoding="utf-8")
#<2>.关闭文件 f.close()
#<3>.f.read()  f.readline()   f.readlines()
#<4>.f.wirte()
#<5>.其他的两个函数 f.tell()  f.seek()


