'''
import test.moduleA  as mA
s1=mA.Stu('zhangsan',19)
s1.show()
'''
#os模块
import  os # 是用来进行办公的，做一些表，一些文件夹之类的
#使用os模块创建一个文件夹

#定义一个变量,用来代表要创建的文件夹的名字
folder_name='new_folder'
#用来检查你要的文件夹是否存在
if  not os.path.exists(folder_name):
    #当文件夹不存在时,在if分支总创建文件夹
    os.mkdir(folder_name)
else:
    print('Folder already exists')
print("当前目录:",os.getcwd())

dirs = os.listdir( folder_name )
print("dirs:",dirs)


for dir in dirs:
    print(dir)



#sys模块  获取系统相关信息
import sys
#使用sys模块打印python解释器版本
print(f'该文件使用的python解释器版本为:',sys.version)

#终止程序
#sys.exit(0)  #进程终止函数

#math模块
import math
print(math.pi)
a=math.pi
print(math.sin(a))

print("2的10次方",math.ceil(math.pow(2,10)))#2的10次方





#time模块
import  time
start=time.time() #1970到现在的秒数
print("start:",start)
time.sleep(5)  #让程序暂停5秒
stop=time.time()
second=stop-start
print("second:",second)
localtime=time.localtime(time.time())  #获得当地时间
print("localtime:",localtime)
#time()
#localtime(time())
#strftime(localtime())

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


#随机数
import random
print("随机的整数:",random.randint(1,10))

mylist=[1,2,3,4,5]

random.shuffle(mylist) #打乱列表

print(mylist)
