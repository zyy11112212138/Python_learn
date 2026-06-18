s = "helloworld"
print(s[0],s[-10])  #代表同一个数
print('重庆欢迎你'[4])
print('重庆欢迎你'[-1])

print(s[2:7]) #包2不包7
print(s[-8:-3]) #包-8不包-3
print(s[:5]) #默认从0开始
print(s[5:]) #默认切到结尾

print('------------------------------')

#字符串操作
x = '2020年'
y = '北京冬奥会'
z = '上海'
print(x + y)
print(x * 10)
print(10 * x)

print('北京' in y)
print('上海' in y)
