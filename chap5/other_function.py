#1.format
print(format(3.14,'20'))            #数值型默认右对齐
print(format('hello','20'))         #字符串默认左对齐
print(format('hello','*<20'))
print(format('hello','*>20'))
print(format('hello','*^20'))

print(format(3.1415926,'.2f'))      #3.14

print(format(20,'b'))       #10100
print(format(20,'o'))       #24
print(format(20,'x'))       #14

print('-'*40)

#2.len
print(len('helloworld'))            #10
print(len([1,2,3,4,5,6]))           #6

print('-'*40)

#3.id
print(id(10))               #140731720168856
print(id(-10))              #1310971574384
print(id('helloworld'))     #1311006798192

print('-'*40)

#4.eval
print(eval('10 + 20'))          #30
print(eval('10 > 20'))          #False