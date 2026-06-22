s1 = 'hello'
s2 = 'world'

#1.使用+
print(s1 + s2)

#2.str.join()拼接
print(''.join([s1,s2]))      #s1s2之间用空字符串拼接 helloworld
print('*'.join([s1,s2]))     #s1s2之间用*拼接    hello*world
print('*'.join(['hi','python']))              #hi*python
print('你好'.join(['hi','zyy','python']))     #hi你好zyy你好python

#3.直接拼接
print('hello''world')           #helloworld

#使用格式化字符串进行拼接
print('%s%s' % (s1,s2))                 #helloworld
print(f'{s1}{s2}')                      #helloworld
print('{0}{1}'.format(s1,s2))     #helloworld