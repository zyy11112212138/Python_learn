# num = input('一个四位整数：')
#
# num2 = eval(num)
#
# ge = num2%10
# num2 //= 10
# shi = num2%10
# num2 //= 10
# bai = num2%10
# num2 //= 10
# qian = num2%10
# print('个位上的数字：',ge)
# print('十位上的数字：',shi)
# print('百位上的数字：',bai)
# print('千位上的数字：',qian)

print('-'*40)

height1 = eval(input('父亲的身高：'))
height2 = eval(input('母亲的身高：'))
print('预测儿子的身高：',(height1 + height2)*0.54)
