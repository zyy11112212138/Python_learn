#判断是否是闰年
# year = eval(input('请输入一个年份：'))
# if (not year%4 and year%100) or year%400:
#     print(year,'是闰年')
# else :
#     print(year,'不是闰年')

#模拟10086查询功能
# while True :
#     print('1.显示当前余额')
#     print('2.显示当前剩余流量')
#     print('3.显示当前剩余话费')
#     print('0.退出查询')
#     x = input('请输入您想查询功能的编号:')
#     match x:
#         case '1':
#             print('当前余额为211.19元')
#         case '2':
#             print('当前剩余流量100000GB')
#         case '3':
#             print('当前剩余通话时长19分钟')
#         case '0':
#             print('欢迎下次光临，再见')
#             break
#         case _:
#             print('您输入的数字有误，请重新输入')

#输出九九乘法表
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(i,'*',j,'=',i*j,end = '\t')
#     print()

#猜数游戏
import random
rand = random.randint(1,100)
while True:
    num = eval(input('请输入1~100的数：'))
    if num < rand:
        print('猜小了，重新猜')
    elif num > rand:
        print('猜大了，重新猜')
    else :
        print('恭喜你，猜对啦！！')
        break

