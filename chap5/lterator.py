print('-'*20 + 'sorted' + '-'*20)

lst = [54,56,77,19,123,66]
print('原序列lst:',lst)
#1.排序操作
asc_lst = sorted(lst)
desc_lst = sorted(lst, reverse=True)
print('升序：',asc_lst)
print('降序：',desc_lst)

print('-'*20 + 'reversed' + '-'*20)

#2.reverse反向
new_lst = reversed(lst)
print(type(new_lst))            #<class 'list_reverseiterator'>  得到的是对象
print(list(new_lst))

print('-'*20 + 'zip' + '-'*20)

#3.zip
x = ['a','b','c','d']
y = [10,20,30,40,50]
zipobj = zip(x,y)
print(type(zipobj))             #<class 'zip'>  得到的是对象
#print(list(zipobj))             #[('a', 10), ('b', 20), ('c', 30), ('d', 40)]

print('-'*20 + 'enumerate' + '-'*20)

#4.enumerate
print('y:',y)
enum = enumerate(y,start = 1)
print(type(enum))               #<class 'enumerate'>
print(tuple(enum))              #[(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]

print('-'*20 + 'all' + '-'*20)

#5.all 布尔值 是否都为True
lst2 = [10,20,'',30]
print('lst2:',lst2)
print(all(lst2))
print(all(lst))

print('-'*20 + 'any' + '-'*20)

#6.any 布尔值 是否存在True（都是False 返回值才是False）
print(any(lst2))
print(any(lst))
print(any(['','']))         #False

print('-'*20 + 'next' + '-'*20)

#7.next 获取迭代器的下一个元素
print(next(zipobj))             #('a', 10)
print(next(zipobj))             #('b', 20)
print(next(zipobj))             #('c', 30)
print(next(zipobj))             #('d', 40)

print('-'*20 + 'filter' + '-'*20)

#8.filter 通过指定条件过滤并返回一个迭代器对象
def fun(num):
    return num % 2 == 0         #可能是True，也可能是False

obj = filter(fun, range(10))        #0-9的数都执行一次fun操作
print(list(obj))                #[0, 2, 4, 6, 8]

print('-'*20 + 'map' + '-'*20)

#map对可迭代器的对象进行操作，并返回一个迭代器对象
def upper(x):
    return x.upper()
lst3 = ['hello','world']
print('lst3:',lst3)
obj2 = map(upper, lst3)
print('map_lst3:',list(obj2))