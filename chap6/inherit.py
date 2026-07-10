class Person:       #省略括号不写，默认继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'大家好，我叫{self.name},我今年{self.age}岁了')

#Student继承Person类
class Student(Person):
    #编写初始化的方法
    def __init__(self, name, age, gender):
        super().__init__(name, age)         #调用父类的初始化方法，给name和age赋值
        self.gender = gender

#Doctor继承Person
class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

stu = Student('zyy',19,'女')
stu.show()

doc = Doctor('lry',20,'中医')
doc.show()
