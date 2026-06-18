#遍历字符串
for i in 'hello':
    print(i)

#range(n，m)函数 生成包含n但不包含m的整数序列
for i in range(1,11):
    if not i%2:
        print(i , '是偶数')

# 计算累加合
sum = 0;
for i in range(1,11):
    sum += i

else :print('1~10的合为：',sum)

#判断100~999之间的水仙花数： 各个位上的立方和等于该数
for i in range(100,1000):
    if i == (i%10)**3 + (i//10%10)**3 + (i//100)**3:
        print(i,'是水仙花数')