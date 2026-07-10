#import  包名 . 模块名   as  别名       会自动调用  init  中的
import admin.my_admin as md
md.info()

print('-'*40)

#from  包名  import  模块名  as  别名     这种方法不会自动调用  init  中的
from admin import my_admin as a
a.info()

print('-'*40)

#导入具体函数
from admin.my_admin import info
info()

print('-'*40)

from admin.my_admin import *
print(name)