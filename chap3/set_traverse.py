s = {1,2,3,4,5,6}
print(s)

#遍历
#1.直接for
for item in s:
    print(item)

#使用enumerate
for index,item in enumerate(s,start = 0):
    print(index,'-->',item)

#生成式
s = {i for i in range(1,10)}
print(s)

s = {i for i in range(1,10) if not i%2}
print(s)