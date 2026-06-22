#判断车牌归属地
import re

lst = ['京A8888','津B66666','渝C88888']
pattern = '[\u4e00-\u9fa5]'

for item in lst:
    pos = re.search(pattern,item)
    if pos:
        print(item,'归属地',pos.group())
    print()