''''''
'''
实现能计算类似 
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式的计算器程序
1、去掉所有的空格
2、加减乘除 括号
3、先算括号里的乘除、再算括号里的加减
4、从括号里取值 == 正则表达式
a = 9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14
从一个没有括号的表达式中取 */法，+-法

'''
import re

def simply(express):
    # if '+-' in express:
    express = express.replace('+-', '-')
    # if '--' in express:
    express = express.replace('--', '+')
    return express


def cal_exp_son(exp_son):
    # 只用来计算最小的表达式
    if '/' in exp_son:
        a, b = exp_son.split('/')
        return str(float(a) / float(b))
    elif '*' in exp_son:
        a, b = exp_son.split('*')
        return str(float(a) * float(b))

def cal_express_no_bracket(exp):
    ''' 计算没有括号的表达式 '''
    ''' exp是没有经过处理的最内层带括号的表达式 '''
    exp = exp.strip('()')
    print('exp:',exp)

    # 先乘除、后加减
    while True:
        ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', exp)
        if ret:  # 表达式中还有乘除法
            exp_son = ret.group()   # 子表达式，最简单的乘除法
            print('exp_son:',exp_son)  # 40/5
            ret = cal_exp_son(exp_son)
            exp = exp.replace(exp_son, ret)
            print('new_exp:', exp)  # -8.0
            exp = simply(exp)

        else:   # 说明表达式中没有乘除法
            ret = re.findall('-?\d+\.?\d*', exp)
            sum = 0
            for i in ret:
                sum += float(i)
            print('***', ret)
            return str(sum)




''' 提取括号里面没有其他括号的表达式 '''
def remove_bracket(new_express):
    while True:

        ret = re.search('\([^()]+\)', new_express)
        # ret = re.findall('\([^()]+\)', new_express)
        # print(ret)
        if ret:
            express_no_bracket = ret.group()
            print(express_no_bracket)
            ret = cal_express_no_bracket(express_no_bracket)
            print(new_express, express_no_bracket, ret, sep=' | ')
            new_express = new_express.replace(express_no_bracket, ret)
            new_express = simply(new_express)
            print(new_express)

        else:
            print('表达式中没有括号了：',new_express)
            ret = cal_express_no_bracket(new_express)
            print(ret)
            return ret



express = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
new_express = express.replace(' ', '')
print(new_express)

res = remove_bracket(new_express)
print(res)