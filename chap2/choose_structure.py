a = 10
b = 4
if a > b:print('a > b')

x = input('输入一个字符串：')
if not x:
    print('x是空字符串')

#双分支
if a > b:
    print('a > b')
else :
    print('a < b')

#使用条件表达式简化（类似于三目运算符）
#例1
print('a > b' if a > b else 'a <= b')

#例2
lucky_number = 987654
num = eval(input('请输入一个6位数字：'))
result = '恭喜您中奖了' if num == lucky_number else '您未中奖'
print(result)

print('-'*40)
#或直接写不用赋值
print('恭喜您中奖了' if num == lucky_number else '您未中奖')

print('-'*40)

#多分支
score = eval(input('请输入您的成绩：'))
if score < 0 or score > 100:
    print('您输入的成绩有误！')
elif score >= 60 and score <=100:
    print('您及格了！')
else:
    print('您未及格！')

print('-'*40)

#嵌套使用
answer = input('你喝酒了没：')
if answer == 'yes' :
    proof = eval(input('酒精含量：'))
    if proof < 20:
        print('未构成酒驾')
    elif proof < 80:
        print('已经是酒驾了')
    else :
        print('醉驾！很危险！')
else :
    print('没喝酒请走')