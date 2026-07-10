class Circal():
    def __init__(self,r):
        self.r = r

    def get_area(self):
        print('圆的面积是：',3.14*(self.r**2))

    def get_perimeter(self):
         print(f'圆的周长是：',2*3.14*self.r)

r = eval(input('请输入圆的半径是：'))
ci = Circal(r)
ci.get_area()
ci.get_perimeter()