lst = [
    ['G1569','北京南-天津南','18:06','18:39','00:33'],
    ['G1567','北京南-天津南','18:15','18:49','00:34'],
    ['G8917','北京南-天津西','18:20','19:19','00:59'],
    ['G203','北京南-天津南','18:35','19:09','00:34']
]

print('车次        出发站-到达站    出发时间    到达时间间隔   历时时长')

for row in lst:
    for item in row:
        print(item,end = '\t\t')
    print()
while True:
    num = input('请输入您要购买的车次：')

    flag = False
    for i in range(4):
        if num == lst[i][0]:
            flag = True
            break

    if not flag:
        print('输入车次有误，请重新输入')
    else :
        break

person = input('请输入乘车人，如果是多位乘车人使用逗号分隔：')

print('您已购买了' + num + ' ' + lst[i][1] + '  ' + lst[i][2] + '开，请' + person + '尽快取纸质车票。【铁路客服】')
