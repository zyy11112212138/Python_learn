try:
    gender = input('请输入您的性别：')
    if gender != '男' or gender != '女':
        raise Exception('性别只能是男或女')         #抛出异常对象，被后面的Exception捕获
except Exception as e:
    print(e)

#成绩必须在0-100之间
try:
    score = int(input('请输入分数：'))
    if score < 0 or score > 100:
        raise Exception('分数不正确')
except Exception as e:
    print(e)

#是否可以构成三角形
try:
    a = int(input('请输入第一条边：'))
    b = int(input('请输入第二条边：'))
    c = int(input('请输入第三条边：'))

    if a + b > c and a + c > b and b + c > a:
        print('三角形的边长为：'+'a={0},b={1},c={2}'.format(a, b, c))
    else :
        raise Exception('a={0},b={1},c={2}'.format(a, b, c) + '不能构成三角形')
except Exception as e:
    print(e)