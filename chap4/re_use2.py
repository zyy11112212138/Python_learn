import re
#sub
pattern = '黑客|破解|反爬'
s = '我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗'

new_s = re.sub(pattern,'XXX',s)
print(new_s)

#split
s2 = 'https://www.baidu.com/s?wd=geek官网&rsv_spt=1&rsv_iqid=0x82dd04ed004ce291'
pattern2 = '[?|&]'
lst = re.split(pattern2,s2)
print(lst)