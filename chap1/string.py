city = '重庆'
address = "重庆市开州区"   #单双引号都可以
print(city)
print(address)

#定义多行字符串(三单或双引号)
info = '''地址：重庆市
    收件人：曾垚垚
    手机号：12345678910
'''

info2 = """地址：重庆市
    收件人：曾垚垚
    手机号：12345678910
"""
print(info)
print(info2)

#转义字符的使用
print('重庆\n欢迎你')  #遇到\n就换行
print('重庆\t欢迎你')
#使转义字符失效 在前面加上r或者R 就会原样输出了
print(r'重庆\n欢迎你')


