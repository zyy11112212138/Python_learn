s = 'helloworldhllooorwdabcfdlow'
#1.字符串拼接+not in
new_s1 = ''
for item in s:
    if item not in new_s1:
        new_s1 +=item         #拼接
print(new_s1)

#2.索引+not in
new_s2 = ''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2 +=s[i]
print(new_s2)

#3.通过集合去重+通过列表排序
new_s3 = set(s)
lst = list(new_s3)
lst.sort(key = s.index)         #表示方法本身，但不调用执行
print(''.join(lst))