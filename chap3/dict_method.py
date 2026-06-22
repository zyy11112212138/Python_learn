d = {99:'c语言',88:'Java',100:'Python'}
print(d)

#添加新元素
d[98] = 'go'
print(d)

#获取所有的key
keys = d.keys()
print(keys)        #获取到的是对象  dict_keys([99, 88, 100, 98])
#得到每一个：
print(list(keys))
print(tuple(keys))

#获取所有的value
values = d.values()
print(values)     #获取到的也是对象   dict_values(['c语言', 'Java', 'Python', 'go'])
#查看具体的：
print(list(values))
print(tuple(values))

#将字典当中的数据转成key-value的形式
lst = list(d.items())
print(lst)              #一个列表 列表里的元素都是元组 [(99, 'c语言'), (88, 'Java'), (100, 'Python'), (98, 'go')]

d = dict(lst)       #转成字典型
print(d)            #{99: 'c语言', 88: 'Java', 100: 'Python', 98: 'go'}

#使用pop
print(d.pop(88))            #Java
print(d)        #先pop出来再进行删除

#随机删除popitem        解释器更新后字典变得有序了 删除的都是最后一个元素了
print(d.popitem())          #元组类型  (98, 'go')
print(d)

#清空
d.clear()
print(d)

#python中一切皆对象，每个对象都有一个布尔值
print(bool(d))       #空字典为False
