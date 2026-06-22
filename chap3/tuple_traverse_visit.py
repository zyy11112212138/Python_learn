t = ('hello','zyy','python','world')
#根据索引直接访问
print(t[1])

#切片访问
t2 = t[0:5:2]
print(t2)

#元组的遍历
#1.for
for item in t:
    print(item)

print('-'*40)

#2.for range
for i in range(len(t)):
    print(i,t[i])

print('-'*40)

#3.enumerate
for index,item in enumerate(t,start = 1):
    print(index,'-->',item)
