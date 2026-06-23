#从字符串中提取数字并计算累加和
s = input('请输入一个字符串：')

lst = []

for i in s:
    if i.isdigit():
        lst.append(int(i))

print('提取的数字列表为：',lst)

def get_sum(lst):
    sum = 0
    for item in lst:
        sum += int(item)
    return sum

print(get_sum(lst))