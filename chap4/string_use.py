#大小写转换
s1 = 'HelloWorld'
low_s1 = s1.lower()
high_s1 = s1.upper()
print(low_s1)
print(high_s1)

#字符串的分隔
s2 = 'zyy@qq.com'
lst = s2.split('@')       #以@分隔 形成两个列表
print(lst[0],lst[1])

#统计子串出现的次数
print(s1.count('l'))      #l在是中出现的次数

#查询操作
print(s1.find('o'))       #o首次出现的位置
print(s1.find('p'))       #-1,没有找到

#与find相似
print(s1.index('o'))
#print(s1.index('p'))            #找不到时会报错    ValueError: substring not found

#判断前后缀
print(s1.startswith('H'))        #Ture
print(s1.startswith('l'))        #False

print('tsxt.txt'.endswith('.txt'))      #True
print('tsxt.txt'.endswith('.md'))       #False

#替换
re_s1 = s1.replace('o','换',1)
print(re_s1)

#字符串在指定范围内居中
print(s1.center(20))            #总长度20
print(s1.center(20,'*'))

#去掉左右空格
s3 = '   hello   zyy   '
print(s3.strip())
#去掉左侧空格
print(s3.lstrip())
#去掉右侧空格
print(s3.rstrip())

#去掉指定字符
s4 = 'dl-helloworld'
print(s4.strip('ld'))       #与顺序无关只要包含就会去掉     -hellowor
print(s4.lstrip('ld'))      #-helloworld
print(s4.rstrip('dl'))      #dl-hellowor