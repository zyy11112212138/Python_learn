#使用（）直接创建
t = ('hello',[10,20,30],'python','world')
print(t)

#使用内置函数tuple( )创建元组
t2 = tuple('helloworld')
print(t2)

t3 = tuple([10,20,30,40])
print(t3)

#是序列的一种 也可以用序列的方法
print('10在元组中是否存在：',10 in t3)
print('10在元组中是否不存在：',10 not in t3)

print('t3元组最大值：',max(t3))
print('t3元组最小值：',min(t3))

print('元素个数：',len(t3))
print('index:',t3.index(20))
print('count:',t3.count(30))

#只有一个元素的时候 逗号也不可以省略
t4 = (10)
print(type(t4))            #int
t4 = (10,)
print(type(t4))            #元组

#删除
del t4
