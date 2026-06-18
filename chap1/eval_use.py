s = '3.14 + 3'
print(s,type(s))

x = eval(s)         #把 '' 打开
print(x,type(x))     #进行了运算

#常和input一起使用  用来获取输入的数值
age = eval(input('请输入您的年龄：'))    #将字符串类型转换成了int型 == int(age)
print(age,type(age))

height = eval(input('请输入您的身高：'))
print(height,type(height))

hello = '重庆'
print(hello)
print(eval('hello'))  # ======print('重庆')
print(eval(hello))    #会报错    NameError: name '重庆' is not defined   =====    print(重庆)   重庆未定义


