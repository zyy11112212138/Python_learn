class Student:
    #类属性，定义在类中，方法外的变量
    school = '湖科大'

    #初始方法
    def __init__(self, name, age):      #name,age是方法的参数，是局部变量，作用域是整个__init__方法
        #类的实例属性
        self.name = name            #将局部变量的值name赋值给实例属性self.name
        self.age = age

    #定义在类中的方法，称为实例方法，自带一个参数self
    def show(self):
        print(f'我叫：{self.name},今年:{self.age}岁了')

stu1 = Student('zyy',19)
stu2 = Student('sc',18)
stu3 = Student('lyy',20)
stu4 = Student('zzw',21)

lst = [stu1,stu2,stu3,stu4]

for item in lst:
    item.show()