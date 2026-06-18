score = input('请输入您的成绩：')
match score :
    case 'A':
        print('您的等级为A')
    case 'B':
        print('您的等级为B')
    case 'C':
        print('您的等级为C')
    case 'D':
        print('您的等级为D')
    case _:
        print('您的等级不属于ABCD而是：' + score)