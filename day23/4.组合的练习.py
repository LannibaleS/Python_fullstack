from math import pi
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r**2*pi

    def perimeter(self):
        return self.r*2*pi


class Ring:
    def __init__(self, outside_r, inside_r):
        self.outside = Circle(outside_r)
        self.inside = Circle(inside_r)

    def area(self):
        return self.outside.area() - self.inside.area()

    def perimeter(self):
        return self.outside.perimeter() + self.inside.perimeter()

ring = Ring(20, 10)
print(ring.area())
print(ring.perimeter())

'''创建一个老师类，生日，生日也可以是一个类，年月日'''


class Course:
    language = ['chinese']
    def __init__(self, teacher, course_name, period, price):
        self.teacher = teacher
        self.course_name = course_name
        self.period = period
        self.price = price


class Birthday:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def birth(self):
        print(self.year, self.month, self.day)

class Teacher:
    def __init__(self, birthday):
        self.birthday = birthday
        self.course = Course('ls', 'python', '6 months', 20000)

ls = Teacher(Birthday(1992, 3, 22))
print(ls.birthday.year)
ls.birthday.birth()

print(ls.course.course_name)