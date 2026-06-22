#try_except_else
try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入一个整数：'))
    result = num1 / num2

except ZeroDivisionError:
    print('除数为0')
except ValueError:
    print('不能将字符串转成整数')
except BaseException:
    print('未知异常')
else:
    print(result)

#try_except_else_finally
try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入一个整数：'))
    result = num1 / num2

except ZeroDivisionError:
    print('除数为0')
except ValueError:
    print('不能将字符串转成整数')
except BaseException:
    print('未知异常')
else:
    print(result)
finally:
    print('程序执行结束')