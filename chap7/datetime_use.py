from datetime import datetime       #从datetime模块中导入datetime类
dt = datetime.now()
print('当前的系统时间：',dt)

print('-'*40)

#datetime是一个类，可以手动创建这个类的对象
dt2  = datetime(2026,6,27,22,44)
print('dt2的数据类型:',type(dt2))
print('dt2的日期时间：',dt2)
print('年：',dt2.year,'月：',dt2.month,'日：',dt2.day)
print('时：',dt2.hour,'分：',dt2.minute,'秒：',dt2.second)

print('-'*40)

#比较两个datetime类型对象的大小 直接使用  <  >
d1 = datetime(2026,5,1)
d2 = datetime(2026,10,1)
print('2026.5.1 比 2026.10.1 早吗？',d1 < d2)           #True

print('-'*40)

#datetime类型与字符串进行转换
nowdt = datetime.now()
nowdt_str = nowdt.strftime('%Y-%m-%d %H:%M:%S')
print('nowdt的数据类型:',type(nowdt),'nowdt所表示的数据：',nowdt)
print('nowdt_str的数据类型:',type(nowdt_str),'nowdt_str所表示的数据：',nowdt_str)

print('-'*40)

#字符串转成datetime类型
str_datetime = '2026年5月2日 22点55分'
d3 = datetime.strptime(str_datetime,'%Y年%m月%d日 %H点%M分')
print('str_datetime的数据类型:',type(d3),'str_datetime所表示的数据：',d3)