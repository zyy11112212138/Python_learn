#import  模块名称 [as  别名]
import my_info
print(my_info.name)
my_info.info()

import my_info as mi
print(mi.name)
mi.info()

#from  模块名称  import  变量 / 函数 / 类 / *
from my_info import name
print(name)

from my_info import info
info()

#*（通配符，会导入所有）
from my_info import *
print(name)
info()

#同时导入多个模块用逗号
import math,random,time