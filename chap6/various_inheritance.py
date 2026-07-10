class FatherA():
    def __init__(self, name):
        self.name = name

    def showA(self):
        print('父类A的方法')

class FatherB():
    def __init__(self, age):
        self.age = age

    def showB(self):
        print('父类B的方法')

class Son(FatherA, FatherB):
    def __init__(self, name, age, gender):
        #调用两个父类的方法，不能直接写super了，要用父类的名称进行区分（父类名称打点）
        FatherA.__init__(self, name)
        FatherB.__init__(self, age)
        self.gender = gender

s = Son('zyy',19,'女')
s.showA()
s.showB()