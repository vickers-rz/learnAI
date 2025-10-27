#打开文件
f=open('1.txt','r')

#<1>.按字节数读取
#readstr1=f.read(20)
#print(readstr1)

#统计该文件有多少行
'''
line=0
#<2>.按行读取
while True:
    readStr2=f.readline()
    if not readStr2:
        break
    print(readStr2)
    line+=1

print(f"该文件有{line}行")
'''
readstr3=f.readlines() #读取文件的所有内容
print(readstr3)
#关闭文件
f.close()