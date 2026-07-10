from datetime import datetime
from datetime import timedelta
#进行两个datetime对象的加减运算
#创建两个datetime对象
delta1 = datetime(2029,9,1) - datetime(2025,9,1)
print('delta1的数据类型：', type(delta1),'delta1所表示的数据：', delta1)         #datetime.timedelta   1461 days, 0:00:00

#通过传入参数的方式创建一个timedelta对象
td1 = timedelta(10)
print('创建一个10天的timedelta对象：',td1)           #10 days, 0:00:00

td2 = timedelta(10,11)
print('创建一个10天11秒的timedelta对象：',td2)        #10 days, 0:00:11