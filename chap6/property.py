class Student():
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender      #self.__gender是私有的实例属性

    #试用装饰器（@property）修改方法，讲方法转成属性使用
    @property
    def gender(self):
        return self.__gender

    #将gender这个属性设置为可写属性
    @gender.setter
    def gender(self,value):
        if value != '男' and value != '女':
            print('输入的性别有误，已将性别默认为女')
            self.__gender = '女'
        else :
            self.__gender = value

stu = Student('zyy','女')

print(stu.name,'的性别是',stu.gender)           #会执行stu.gender()这个方法
#只可以查看，但不可以修改
#stu.gender = '男'            #AttributeError: property 'gender' of 'Student' object has no setter

#想要赋值的话，还需要setter
stu.gender = '其他'
print(stu.gender) 