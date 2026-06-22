#格式化输出商品名称和单价
goods = [
    ['01','电风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','老板',400],
]

print('编号     名称        品牌     单价')

for row in goods:
    for item in row:
        print(item,end = '\t\t')
    print()

for item in goods:
    item[0] = '{0:0>6}'.format(item[0])
    item[3] = '${0:.2f}'.format(item[3])

print('编号         名称        品牌      单价')
for row in goods:
    for item in row:
        print(item,end = '\t\t')
    print()