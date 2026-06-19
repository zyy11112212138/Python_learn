lst = []

for i in range(5):
    goods = input('请输入商品的编号和商品的名称进行入库，每次只能输入一件商品：')
    lst.append(goods)

for i in range(len(lst)):
    print(lst[i])

buy = []

while True:
    info = input('请输入您要购买的商品的编号：')

    flag = False
    for i in lst:
        if info == i[0:4]:
            flag = True
            buy.append(i)
            print('商品已成功添加到购物车')
            break

    if flag == False and info != 'q':
        print('商品不存在')

    if info == 'q':
        break

    print('-' * 50)

print('购物车里已选择的商品为：')
buy = reversed(buy)
for index,value in enumerate(buy):
    print(value)