#1.d = {key:value for item in range }
import random

d = {item : random.randint(1,100) for item in range(4)}   #key:item   value:1~100随机数
print(d)

#2.d = {key:value for key,value in zip(lst1,lst2)}
#创建两个列表
lst1 = [10,20,30]
lst2 = ['cat','dog','bird']

d = {key:value for key,value in zip (lst1,lst2)}
print(d)