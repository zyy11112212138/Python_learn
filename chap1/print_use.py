a = 211
b = 321
print(a)
print(a + b)

#会自动换行
print('hello')
print("hello")
print('''hello''')
print("""hello""")

#不换行(","-->空格)
print(a,b,'pig')

#输出ASCII对应字符(使用chr)
print(chr(98),chr(56),chr(67))

#Unicode(使用ord)
print(ord('刘'),chr(21016))

#多条输出 结果在一行显示
print('垚垚',end = '-->')  #将 结束符 修改成了 -->
print('你好呀')  # 没有修改结束符 还是换行

#使用连接符(+) 连接字符
#只能字符串和字符串连接 不能和数字连接
print("现在是" + "2026")