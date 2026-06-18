x = 10
y = 3
z = x/y
print(z,type(z))    #3.3333333333333335    float  隐式类型转换

#float转成int  只保留整数部分
print('3.14转成int:',int(3.14))       #3
print('-3.9转成int:',int(-3.9))     #-3

#将int转成float
print('10转成float:',float(10))

#将str转成int
print(int('100') + int('200'))

#将str转成int会报错的情况
#print(int('19a'))     #ValueError: invalid literal for int() with base 10: '19a'
#print(int('3.14'))     #ValueError: invalid literal for int() with base 10: '3.14'
#print(float('34a.987'))     #ValueError: could not convert string to float: '34a.987'

#chr(),ord()一对逆运算，ord算出对应值，chr转成对应字符
print(ord('垚'))    #22426
print(chr(22426))

#进制之间的转换操作
#转换后是字符串类型
print('22426转成十六进制',hex(22426))
print('22426转成八进制',oct(22426))
print('22426转成二进制',bin(22426))

print(type(hex(22426)))      #字符串类型

