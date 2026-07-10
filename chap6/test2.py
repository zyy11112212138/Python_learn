class Student():
    def __init__(self,name,age,gender,score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def info(self):
        print('姓名：',self.name,'年龄：',self.age,'性别：',self.gender,'分数：',self.score)

print('请输入5位学生信息：姓名#年龄#性别#成绩')

lst = []
for i in range(1,6):
    s = input(f'请输入第{i}位学生信息:')
    s_lst = s.split('#')

    stu = Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])

    lst.append(stu)

for item in lst:
    item.info()