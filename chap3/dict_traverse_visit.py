d = {'c语言':99,'Java':88,'Python':100}
#访问元素
#1.d[key]
print(d['Python'])

#2.d.get[key]
print(d.get('c语言'))

#区别：若key不存在 d.[key]会报错，而d.get[key]可以指定默认值
#print(d['go'])            #KeyError: 'go'
print(d.get('go'))         #None
#指定默认值
print(d.get('go','可以指定默认值'))        #可以指定默认值

#遍历
#1.for element in d.items( ):
for item in d.items():
    print(item)             #由key和value组成一个元组类型

#2.分别获取key和value
for key,value in d.items():
    print(key,'--->',value)
