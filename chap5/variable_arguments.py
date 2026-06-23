#个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

#调用
fun(10,20,30,40)       #<class 'tuple'>
fun(10)                      #<class 'tuple'>
fun([10,20,30,40])           #<class 'tuple'>    列表看做一个整体，还是元组，实际上传递了一个参数

#调用前加一颗*：将列表进行解包
fun(*[10,20,30,40])          #<class 'tuple'>


#个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key, value in kwpara.items():
        print(key,'-->',value)

#调用
fun2(name = '曾垚垚',age = 19,height = 185)            #<class 'dict'>

d = {'name':'曾垚垚','age':19,'height':185}
#fun2(d)             #报错   TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)           #系列解包