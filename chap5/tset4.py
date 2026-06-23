#用函数实现in的功能
s = input('请输入一个字符串：')

lst = ['hello','world','python']

def isin(s,lst):
    for item in lst:
        if s == item:
            return True
    return False

print('存在' if isin(s,lst) else '不存在')