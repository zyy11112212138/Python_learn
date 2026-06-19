#直接创建
lst1 = ['zyy','19','250504']
print(lst1)

#使用list
lst2 = list('helloworld')
print(lst2)

#列表是序列的一种 也可以用序列的方法
lst3 = list(range(1,10,2))
print(lst3)
print(lst1 + lst2 + lst3)

print(len(lst1))
print(max(lst1))
print(min(lst1))
print(lst2.count('o'))

#删除操作
del lst3

#列表的遍历
lst4 = ['hello','zyy','python']

#1.for循环
for index in lst4:
    print(index)

#2.for + range
for i in range(0,len(lst4)):
    print(i,'-->',lst4[i])

#3.enumerate
for index,item in enumerate(lst4):
    print(index,item)
#可以改变起始位置
for index,item in enumerate(lst4,start = 1):   #或：for index,item in enumerate(lst4,1):
    print(index,item)
