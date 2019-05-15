#参数
    #没有参数
        #定义函数和调用函数时括号里都不写内容
    #有一个参数
        #传什么就是什么
    #有多个参数
        #位置参数
def my_sum(a,b,c):
    print(a,b,c)
    res = a+b+c  #result
    return res

ret = my_sum(1,c=2, b=3)
print(ret)

#站在实参的角度上：
    #按照位置传参
    #按照关键字传参
    #混着用可以:但是 必须先按照位置传参，再按照关键字传参数
            #  不能给同一个变量传多个值

'''
#站在形参的角度上
    #位置参数：必须传,且有几个参数就传几个值
    #默认参数: 可以不传，如果不传就是用默认的参数，如果传了就用传的
    
'''

def classmate(name, sex='male'):
    print('{}:{}'.format(name, sex))

classmate('ls')
classmate('hez', 'female')

