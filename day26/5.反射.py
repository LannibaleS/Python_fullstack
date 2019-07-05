''''''
'''
反射
'''

class Teacher:
    dic = {'查看学生信息':'show_student', '查看讲师信息':'show_teacher'}
    def show_student(self):
        print('show_student')

    def show_teacher(self):
        print('show_teacher')

    @classmethod
    def func(cls):
        print('hhahahah')
'''
hasattr | getattr | delattr 
'''

ls = Teacher()
for k in Teacher.dic:
    print(k)
key = input('输入需求:')
if hasattr(ls, Teacher.dic[key]):
    func1 = getattr(ls, Teacher.dic[key])
    func1()

print('\n===============')
func = getattr(ls,'show_student')
func()

if hasattr(Teacher, 'dic'):
    ret = getattr(Teacher, 'dic')      # Teacher.dic 类也是对象
    print(ret)
ret2 = getattr(Teacher, 'func')    # Teacher.func 类也是对象
print(ret2)

'''
通过反射
对象名 获取对象属性 和 普通方法
类名 获取静态属性 和类方法 静态方法

普通方法 self
静态方法 @staticmethod
类方法   @classmethod
属性方法 @property
'''

'''
继承
封装
'''