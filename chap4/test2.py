#统计字符串中出现指定字符的次数,忽略大小写
s = 'HelloPython,HelloJava,HelloC'

char = input('请输入要统计的字符：')

if ord(char) >= 65 and ord(char) <= 90:
    print('{0}在{1}一共出现了{2}次'.format(char,s,s.upper().count(char)))

else :
    print('H{0}在{1}一共出现了{2}次'.format(char, s, s.lower().count(char)))