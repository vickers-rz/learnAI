
class Person:
    def __init__(self, name, age,height):
        self.name = name
        self.age = age
        self.height=height

    def show(self):
        print(self.name, self.age)


class Stu(Person):
    def __init__(self, name,age,height,score):
        #self.name = name
        #self.age = age
        #self.height=height
        super().__init__(name,age,height)
        self.score = score

    def show(self):
        print(self.name, self.age, self.score)



s1=Stu('zhangsan',19,100)
s1.show()