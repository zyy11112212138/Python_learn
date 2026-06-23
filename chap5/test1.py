#计算列表中函数的最大值
import random
lst = []
for i in range(10):
    lst.append(random.randint(1,100))
print(lst)

def m(lst):
    max = lst[0]
    for item in lst:
        if item > max:
            max = item
    return max

print(m(lst))