my_name = '曾垚垚'

lucky_number = 7

print('lucky_number的数据类型是：',type(lucky_number))
print(my_name,'的幸运数字是：',lucky_number)

#Python可以动态修改变量的数据类型，通过赋不同类型的值，就可以直接修改
lucky_number = '重庆'
print('lucky_number的数据类型是：',type(lucky_number))

#允许多个变量指向同一个值
a = b = 19     #a,b都指向了19这个值
print(a,b)
print(id(a))   #id用于查看对象的内存地址
print(id(b))   #a,b地址相同

#浮点型保留小数
print(0.1 + 0.2)
print(round(0.1 + 0.2,1))

#复数
x = 123 + 456j
print('实数部分：',x.real)
print('实数部分：',x.imag)