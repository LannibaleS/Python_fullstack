class Classes:
    def __init__(self, name, school, kind):
        self.name = name     # 班级名称
        self.school = school # 学校
        self.kind = kind     # 班级科目
        self.student = ['student_obj']

class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

c = Course('pyhton', '6 months', 20000)
class Teacher:
    def __init__(self, name, classes, course):
        self.name = name
        self.classes = ['classses_obj']
        self.course = c   # 组合


