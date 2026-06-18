#模拟用户登录 仅三次机会
i = 1
while i<= 3:
    user_name = input('请输入用户名：')
    psw = input('请输入密码：')

    if (user_name == 'zyy11112212138') and (psw == 'zyy'):
        print('登录成功………………')
        break

    else :
        if i <= 2:
            print('您还有',3 - i,'次机会')

    i += 1
else:
    print('三次均错误，您没有机会了！')
#打印图形
#三行四列长方形
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print()                #换行

print('-'*50)

#直角三角形五行
for i in range(1,6):
    for j in range(1,i + 1):
        print('*',end='')
    print()

print('-'*50)

#倒着的直角三角形 五行
for i in range(1,6):
    for j in range(1,7 - i):
        print('*',end='')
    print()

print('-'*50)

#三角形13579
for i in range(1,6):
    for j in range(1,6 - i):
        print(' ',end='')
    for k in range(1,2 * i):
        print('*',end='')
    print()

print('-'*50)

#菱形
a = eval(input('请输入菱形边长：'))
for i in range(1,a + 1):
    for j in range(1,a - i + 1):
        print(' ',end='')
    for k in range(1,2 * i):
        print('*',end='')
    print()

for i in range(1,a):
    for j in range(1,i + 1):
        print(' ',end='')
    for k in range(1,2 * (a - i)):
        print('*',end='')
    print()

print('-'*50)

#空心菱形
b = eval(input('请输入菱形边长：'))
for i in range(1,b + 1):
    for j in range(1,b - i + 1):
        print(' ',end='')
    for k in range(1,2 * i):
        if k == 1 or k == 2 * i - 1:
            print('*',end='')
        else :
            print(' ',end='')
    print()

for i in range(1,b):
    for j in range(1,i + 1):
        print(' ',end='')
    for k in range(1,2 * (b - i)):
        if k ==1 or k == 2 * (b - i) - 1 :
            print('*',end='')
        else :
            print(' ',end='')
    print()