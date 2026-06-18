fp = open('note.txt','w') #打开文件  w-->write

print('北京欢迎你',file = fp)  #将'北京欢迎你' 写入到note.txt中

fp.close()