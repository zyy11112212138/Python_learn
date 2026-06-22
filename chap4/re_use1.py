import re       #导入
#match使用
pattern = '\\d\\.\\d+'   #格式串  数字.数字（一次或多次）
s = 'I study Python 3.14 and 3.11 every day'         #待匹配字符串

match = re.match(pattern,s,re.I)    #忽略大小写
print(match)            #从头开始匹配 字符串开头没有数字   None

s2 = '3.14 Python I study every day'
match2 = re.match(pattern,s2,re.I)
print(match2)                   #<re.Match object; span=(0, 4), match='3.14'>   前包后不包

print('匹配值的起始位置：',match2.start())           #0
print('匹配值的结束位置：',match2.end())             #4
print('匹配值的区间位置：',match2.span())            #(0,4)
print('待匹配的字符串：',match2.string)             #3.14 Python I study every day
print('匹配的数据：',match2.group())                 #3.14

print('-'*60)

#search    找不到就是None
match3 = re.search(pattern,s)           #只找第一个  <re.Match object; span=(15, 19), match='3.14'>
print(match3)
print('匹配的数据：',match3.group())

print('-'*60)

#findall   满足要求的都能找出来   返回一个列表
match4 = re.findall(pattern,s)
print(match4)           #['3.14', '3.11']