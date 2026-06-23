def calc1(a,b):
    print(a + b)

calc1(10,20)
print(calc1(10,20))         #None    无返回值

print('-'*40)

def calc2(a,b):
    s = a + b
    return s

get_s = calc2(10,20)
print(get_s)

get_s2 = calc2(calc2(10,20),30)
print(get_s2)                   #60

def get_sum(num):
    sum = 0
    odd_sum = 0
    even_sum = 0
    for i in range(num):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
        sum += i
    return sum, odd_sum, even_sum           #元组

result = get_sum(10)
print(type(result))                 #<class 'tuple'>
print(result)                   #(45, 25, 20)

#系列解包赋值
a,b,c = get_sum(10)                 #三个值，元组类型
print(a,b,c)            #45 25 20