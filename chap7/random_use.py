#导入
import random
#设置随机数的种子
random.seed(10)
print(random.random())              #[0.0 , 1.0)
print(random.random())              #不会变了

print('-'*40)

#a-b随机整数
print(random.randint(1,100))            #含1，也含100

print('-'*40)

#产生序列
for i in range(10):
    print(random.randrange(1,10,3))         #[start , stop)  步长为3   1 4 7

print('-'*40)

#产生随机小数
print(random.uniform(1,10))             #[a , b] 的随机小数

print('-'*40)

#随机从序列中区元素
lst = [i for i in range(1,11)]
print(random.choice(lst))               #随机种子固定了，重复运行的结果是一样的

print('-'*40)

#随机的排序
random.shuffle(lst)
print(lst)

random.shuffle(lst)
print(lst)                      #两次执行结果不一样