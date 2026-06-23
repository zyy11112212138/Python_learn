#字符的大小写转换
s = input('请输入一个字符串：')

def change(s):
    new_s = ''
    for i in s:
        if 'a'<=i<='z':
            new_s += i.upper()
        elif 'A'<=i<='Z':
            new_s += i.lower()
        else:
            new_s += i
    return new_s

print(change(s))