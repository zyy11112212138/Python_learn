import time
#获取当前时间
now = time.time()               #获取当前的时间戳
print(now)

print('-'*40)

#本地时间
obj = time.localtime()              #会得到一个对象  struct_time
print(obj)

obj2 = time.localtime(60)           #60s        1970年，1月1日，8时，1分，0秒
print(obj2)
#输出具体的
print('年份：',obj2.tm_year)
print('月份：',obj2.tm_mon)
print('日期：',obj2.tm_mday)
print('时：',obj2.tm_hour)
print('分：',obj2.tm_min)
print('秒：',obj2.tm_sec)
print('星期：',obj2.tm_wday)           #星期一默认输出是0
print('今年的多少天：',obj2.tm_yday)

print('-'*40)

print(time.ctime())         #时间戳对应的易读的字符串

print('-'*40)

#日期时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))         #str-->字符串 f-->format time-->时间
print('%B月份的名称',time.strftime('%B',time.localtime()))
print('%A星期的名称',time.strftime('%A',time.localtime()))

print('-'*40)

#字符串转成struct_time对象
print(time.strptime('2008-08-08','%Y-%m-%d'))

print('-'*40)

#休眠 程序暂停
time.sleep(19)
print('停了19s')