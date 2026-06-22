t = (i for i in range(1,4))
print(t)             #不是元组 而是一个生成器对象

#对于生成器对象遍历的话 可以使用__next__()类似于Java中的迭代器
print(t.__next__())         #1
print(t.__next__())         #2
print(t.__next__())         #3

t = tuple(t)         #转成元组
print(t)             #前面遍历完了，这时再输出就是  （）了

#遍历
for item in t:
    print(item)