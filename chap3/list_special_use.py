lst = ['hello','zyy','python']
print('原列表：',lst,id(lst))

#增加元素
lst.append('19')
print('增加元素后：',lst,id(lst))     #内存地址不变

#插入元素
lst.insert(1,'2026')
print('在1处插入元素：',lst)

#删除元素
lst.remove('python')
print('删除元素之后',lst)

#使用pop（index） 先取出后删除
print(lst.pop(3))
print('pop出索引为3的位置后：',lst)

#列表的反向输出
lst.reverse()   #不会产生新的列表，是在原列表的基础上进行的
print('列表反转后：',lst)

#列表的拷贝，产生新列表
new_lst = lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表的修改
#根据索引进行修改
lst[0] = 'zyy11112212138'
print(lst)

#清除所有元素clear
lst.clear()
print(lst)