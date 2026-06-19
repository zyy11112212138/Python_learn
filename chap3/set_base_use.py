#使用{ }直接建
s = {1,2,3,4,5,6}
print(s)

#只能存储不可变数据类型
# s = {[1,2],[3,4],[5,6]}         #TypeError: cannot use 'list' as a set element (unhashable type: 'list')
# print(s)

#使用内置函数set(可迭代对象)创建
s = set()               #创建了一个空集合  空集合的布尔值为False
print(s)
#若直接用s = {}  创建出来的是一个字典类型
s1 = {}
print(type(s1))             #<class 'dict'>

#集合是无序不重复的
s = set('hello')
print(s)

s2 = set([1,2,3])      #可以创建 因为列表是可迭代对象  可迭代：能被循环逐个取出里面元素的对象
print(s2)

s3 = set(range(1,11))
print(s3)

#集合也属于序列的一种 可以使用序列的方法
print('max:',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('是否存在：',7 in s3)
print('是否存在：',7 not in s3)

#删除
del s3