#除数为0
try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入一个整数：'))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('除数为0')

#输入的不是整数
try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入一个整数：'))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('除数为0')
except ValueError:
    print('不能将字符串转成整数')
except BaseException:
    print('未知异常')