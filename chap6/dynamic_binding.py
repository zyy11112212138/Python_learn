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
stu2 = Student('sc',21)

#为stu1动态绑定一个属性
stu1.gender = '女'
print(stu1.name,stu1.age,stu1.gender,stu1.school)       #stu2没有，只有stu1有

#动态绑定方法
def introduce():
    print('我是一个普通的函数，我被动态绑定成了stu1对象的方法')
stu1.fun = introduce        #函数的赋值
#fun就是stu1对象的方法
#调用
stu1.fun()