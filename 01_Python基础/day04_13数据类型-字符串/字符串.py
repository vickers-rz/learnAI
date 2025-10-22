
"""
# 字符串的创建
str1 = '123asdf张三,./;"'
print(str1)

str2 = '''
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''
print(str2)
"""


'''
# 转义字符
print('asdf\'asdfasd\'fasdf')
'''

'''
# 字符串的下标访问
name = 'zhangsan'
print(name[0])
print(name[-1])
print(name[-2])
print(name[100])
'''

'''
# 字符串的切片访问
name = 'zhangsan'
print(name[::])
print(name[0:4:1])
print(name[0:4:2])
print(name[-5::])

# 字符串的逆序
str1 = 'This is a book'
# koob a si sihT
str2 = str1[::-2]
print(str2)
'''

'''
# 两个字符串的比较
# 0：48  1：49  9：57
# A：65 B：66  Z：90
# a：97 b：98  z：122
str1 = 'zhangsan'
str2 = 'lisi'

print(str1 == str2)
print(str1 is str2)
print(id(str1))
print(id(str2))
'''

'''
# 字符串的加法
str1 = 'zhangsan'
str2 = 'lisi'
str3 = 'wangwu'
print(str1 + str2 + str3)

# 字符串的乘法
print(str1 * 2)
'''

'''
# 字符串的查询函数
str1 = "Hello World"
str2 = 'zhangsan'
# print(str1.find('abc'))
# print(str1.index('abc'))
print(str1.rfind('or'))
'''

'''
# 字符串的转换函数，操作对象是字母
str1 = 'zhangsan123,./'
print(str1.upper())
print(str1.title())

str2 = 'ZHANGSAN'
print(str2.lower())
'''

'''
# 字符串的判断函数
str1 = 'zhangsan123 '
print(str1.isalnum())
'''

'''
# 字符串的分割函数
str1 = 'hello world hello China'
# partition()函数 会返回一个元组，如果参数里填写的字符串在源字符串中不存在
# 就会生成两个空字符串及源字符串放到元组中
str2 = str1.partition('o')
str3 = str1.rpartition('o')
print(str2)
print(str3)

# 将字符串根据参数进行分割，可以自定义切割次数
# 如果不指定切割次数，那么会切割所有检测到的地方
print(str1.split(' ', 2))

str4 = 'hello\nhello\nhello'
print(str4.splitlines())
'''



# 其他常用的函数
# count函数
str1 = 'hello world'
print(str1.count('c'))


# join函数
# 序列中的元素必须是字符串才可以连接为新的字符串
str1 = '_'
list1 = ['hello', 'world', 'hello world']
print(str1.join(list1))

# replce函数
str2 = 'hello world hello China'
print(str2.replace('hello', 'Hello'))
print(str2.replace('hello', 'Hello', 1))


# capitalize函数  和 title()函数的作用类似
str3 = 'hello world'
print(str3.capitalize())


# len()函数
print(len(str3))



