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

    #静态方法
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')

    #类方法
    @classmethod
    def cm(cls):     #cls-->class
        print('这是一个类方法，也不能调用实例属性和实例方法')

#创建类的对象
st = Student('zyy',19)      #init方法中有两个形参，所以传两个参数，self是自带的参数，无需手动传入
#实例属性，对象名打点调用
print(st.name, st.age)          #zyy 19
#类属性，直接类名打点调用
print(Student.school)
#实例方法,对象名打点调用
st.show()
#静态方法、类方法，直接使用类名打点调用
Student.sm()
Student.cm()