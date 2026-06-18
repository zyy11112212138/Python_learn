#系列解包赋值
a,b = 10,20
print(a,b)      #10  20

#可用于交换两个变量的值
a,b = b,a
print(a,b)      #20  10

#数据类型会隐式转换
x = 10
y = 5
print(x,type(x))

x /= y
print(x,type(x))

#字符串分解赋值
a,b,c,d = 'room'
print(a)
print(b)
print(c)
print(d)
