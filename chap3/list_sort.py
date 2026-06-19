lst = [3,5,23,19,37,99]
print('原列表',lst)

#1.列表对象的sort方法
lst.sort()              #在原列表基础之上进行，不会产生新的列表
print('升序',lst)
#降序
lst.sort(reverse=True)
print('降序',lst)

lst2 = ['Cat','Dog','age','banana']
lst2.sort()
print('升序',lst2)
lst2.sort(reverse=True)
print('降序',lst2)

#自己制定比较规则
lst2.sort(key = str.lower)
print(lst2)

#2.内置函数sorted
print('原列表',lst)

new_lst1 = sorted(lst)
print('升序',new_lst1)

new_lst2 = sorted(lst,reverse=True)
print('降序',new_lst2)

#忽略大小写
print('原序列',lst2)
new_lst3 = sorted(lst2,key=str.lower)
print(new_lst3)