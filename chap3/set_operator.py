A = {1,2,3,4,5}
B = {3,5,7,8,9}

#交集A&B
print(A&B)
#并集A|B
print(A|B)
#差集A-B
print(A-B)
#补集A^B
print(A^B)

#添加元素
A.add(99)
print(A)
#删除元素
A.remove(2)
print(A)
#清空
A.clear()
print(A)            #空集合的布尔值是False
