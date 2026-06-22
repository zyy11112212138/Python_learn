lst = [88,89,90,98,00,99]
print('原列表：',lst)

# for i in range(len(lst)):
#     if str(lst[i]) == '0' :
#         lst[i] = '200' + str(lst[i])
#     else :
#         lst[i] = '19' + str(lst[i])

for index,value in enumerate(lst):
    if str(lst[index]) == '0' :
        lst[index] = '200' + str(value)
    else :
        lst[index] = '19' + str(value)

print(lst)
