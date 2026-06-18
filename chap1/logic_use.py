#and
#会发生短路  左侧为假  右侧不再进行判断
print(True and True)     #True
print(True and False)    #False
print(False and False)   #False

print('-'*20)

#or
#会发生短路  左侧为真  右侧不再进行判断
print(True or True)      #True
print(True or False)     #True
print(False or False)    #False

print('-'*20)

#not
print(not True)          #False
print(not False)         #True
print(not 8)             #False
