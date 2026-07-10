class Person():
    def eat(self):
        print('人，吃五谷杂粮')

class Cat():
    def eat(self):
        print('猫，吃鱼')

class Dog():
    def eat(self):
        print('狗，吃骨头')

#三个类有同名方法
#函数
def fun(obj):           #不知道形参的类型
    obj.eat()           #不知道obj的数据类型，仍然可以调用eat方法

per = Person()
cat = Cat()
dog = Dog()

fun(per)            #构成了多态，不关心对象的数据类型，只关心对象是否具有同名方法
fun(cat)
fun(dog)