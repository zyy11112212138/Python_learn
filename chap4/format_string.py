#1.占位符
name = '曾垚垚'
age = 19
score = 100.0
print("姓名：%s，年龄：%d，成绩：%.2f" % (name, age, score))

#2.f-string
print(f'姓名：{name}，年龄：{age}，成绩：{score}')

#3.str.format()
print('姓名：{0}，年龄：{1}，成绩：{2}'.format(name, age, score))   #012对应后面的format中的索引位置
print('姓名：{2}，年龄：{0}，成绩：{1}'.format(age,score, name))   #012对应后面的format中的索引位置

#引导符，填充，左对齐，右对齐
s = 'helloworld'
print('{0:*<20}'.format(s))    #显示宽度20，左对齐，多的用*填充
print('{0:*>20}'.format(s))    #显示宽度20，右对齐，多的用*填充
print('{0:*^20}'.format(s))    #显示宽度20，居中对齐，多的用*填充
print(s.center(20,'*'))    #显示宽度20，居中对齐，多的用*填充

#千位分隔符只适用于整数和浮点数
print('{0:,}'.format(9876543210))       #从后往前三位一个逗号
print('{0:,}'.format(9876543.210))       #整数部分三位一个逗号

#浮点数的精度
print('{0:.2f}'.format(1.9211))     #两位小数
print('{0:.5}'.format(s))           #显示宽度5

#整数类型
a = 19
print('二进制：{0:b},十进制：{0:d}，八进制：{0:o}，十六进制：{0:x}，二进制：{0:X}'.format(a))

#浮点数类型
b = 19.211
print('保留小数：{0:.2f},科学计数法：{0:.2E}，科学计数法：{0:.2e}，百分号：{0:.2%}'.format(b))