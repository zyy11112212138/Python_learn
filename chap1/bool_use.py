x = True
print(x)
print(type(x))
print(x + 10)          # 11
print(False + 10)      # 10

#测试对象的布尔值
print(bool(19))         #True
print(bool(0),bool(0.0))    #非0的整数的布尔值都为True
print(bool('曾垚垚'))   #True
print(bool(''))        #False
print(bool(False))      #False
print(bool(None))       #False
