def calc(a,b):
    return a+b

print(calc(10,20))

print('-'*40)

#lambda简化
s = lambda a,b:a + b
print(type(s))              #<class 'function'>
#调用
print(s(10,20))

#列表的取值也能用匿名函数
lst = [10,20,30,40,50]
for i in range(len(lst)):
    result = lambda x:x[i]          #这里的result是函数类型，x是形参
    print(result(lst))              #lst是实参

print('-'*40)

#lambda在排序的时候使用
score = [
    {'name':'张三','score':100},
    {'name':'李四','score':99},
    {'name':'王五','score':92},
    {'name':'刘二','score':97},
]

score.sort(key=lambda x:x.get('score'),reverse=True)            #降序
print(score)