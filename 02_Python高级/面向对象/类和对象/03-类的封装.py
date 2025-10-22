# 私有属性的设置： 在属性名和方法名前添加双下划线前缀

class Person:
    def __init__(self, name, password):
        self.name = name
        self.iphone_id = '135xxxxxxxx'
        self.__password = password

    def __say(self):
        print(f'我的银行卡密码是{self.__password}')

    def change_password(self):
        self.__say()


p1 = Person('zhangsan', '123456')
print(p1.name)
print(p1.iphone_id)
p1.change_password()

