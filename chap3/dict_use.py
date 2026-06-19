#1.使用{ }直接建
d1 = {1:'cat',2:'dog',3:'bird',2:'people'}
print('d1',d1)          #当key相同时，后面的value会覆盖前面的

#2.使用zip函数映射
lst1 = [10,20,30]
lst2 = ['cat','dog','bird','people']

zipobj = zip(lst1,lst2)          #映射出来是一个zip对象
print(zipobj)

#print(list(zipobj))              #[(10, 'cat'), (20, 'dog'), (30, 'bird')]

d2 = dict(zipobj)
print('d2:',d2)           #{10: 'cat', 20: 'dog', 30: 'bird'}

#使用参数创建字典
d3 = dict(cat = 10,dog = 20)
print('d3:',d3)

#元组作为键
t = ('cat','dog','bird','people')
d4 = {t:99}
print('d4',d4)

#列表不可以
# lst = [10,20,30]             #cannot use 'list' as a dict key (unhashable type: 'list')
# print({lst:11})

#是序列的一种 也可以用序列的方法
print('max:', max(d3))
print('min:', min(d3))
print('len:', len(d3))

#删除
del d4