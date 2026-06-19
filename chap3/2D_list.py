#二维列表的创建
lst = [
    ['城市','环比','同比'],
    ['北京',102,122],
    ['上海',342,121],
    ['重庆',123,456]
]
print(lst)

#遍历
for row in lst:
    for item in row:
        print(item,end = '\t')
    print()

#生成一个四行五列的二维列表
lst2 =  [[col for col in range(1,6)]for row in range(1,5)]
print(lst2)