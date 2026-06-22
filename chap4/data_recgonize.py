#只认识十进制阿拉伯数字123
print('123'.isdigit())              #True
print('0b10101'.isdigit())          #False
print('ⅢⅢⅢ'.isdigit())            #False
print('壹贰叁'.isdigit())            #False

print('-'*50)

#所有数字罗马数字，阿拉伯数字，中文壹贰叁(不认识十进制转换后的数，比如二进制)
print('123'.isnumeric())           #True
print('0b10101'.isdigit())         #False
print('ⅢⅢⅢⅢ'.isnumeric())       #True
print('壹贰叁'.isnumeric())         #True

print('-'*50)

#字母（包括中文字）
print('hello'.isalpha())                #True
print('hello曾垚垚'.isalpha())           #True
print('hello曾垚垚123'.isalpha())        #False
print('hello曾垚垚一二三'.isalpha())      #True
print('hello曾垚垚ⅢⅢⅢ'.isalpha())      #False

print('-'*50)

#数字或者字母
print('hello'.isalnum())                #True
print('hello曾垚垚'.isalnum())           #True
print('hello曾垚垚123'.isalnum())        #True
print('hello曾垚垚一二三'.isalnum())      #True
print('hello曾垚垚ⅢⅢⅢ'.isalnum())      #True

print('-'*50)

#中文既是大写也是小写
#字母都是小写吗
print('helloworld'.islower())               #True
print('HelloWorld'.islower())               #False
print('helloworld曾垚垚'.islower())          #True

print('-'*50)

#字母都是大写吗
print('HELLOWORLD'.isupper())               #True
print('HelloWorld'.isupper())               #False
print('HELLOWORLD曾垚垚'.isupper())          #True

print('-'*50)

#是不是只有首字母大写
print('HELLOWORLD'.istitle())               #False
print('HelloWorld'.istitle())               #False
print('Helloworld'.istitle())               #True
print('Hello World'.istitle())              #True
print('Hello world'.istitle())              #False

print('-'*50)

#是否都是空白字符
print('\t'.isspace())                   #True
print(' '.isspace())                    #True
print('\n'.isspace())                   #True