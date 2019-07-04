import re


def math(dic):
    x, y = float(dic['x']), float(dic['y'])
    if dic['mark'] == '+': return x + y
    elif dic['mark'] == '-': return x - y
    elif dic['mark'] == '*':return x * y
    else: return x / y

def cal(re_str):
    ret4 = re.search(r'(?P<x>\d+\.?\d*)(?P<mark>[*/])(?P<y>[\-]?\d+\.?\d*)', re_str)

    try:
        while ret4.group():
            re_str = re_str.replace(ret4.group(), str(math(ret4.groupdict())))
            if '--' in re_str: re_str = re_str.replace('--', '+')
            if '++' in re_str: re_str = re_str.replace('++', '+')
            if '+-' in re_str: re_str = re_str.replace('+-', '-')
            ret4 = re.search(r'(?P<x>[\-]?\d+\.?\d*)(?P<mark>[*/])(?P<y>[\-]?\d+\.?\d*)', re_str)

    except AttributeError: pass




def main(user_inp):
    while True:
        if not re.search('\([^()]\)', user_inp):  #如果表达式中没有括号了
            print(user_inp)
            return cal(user_inp)
        else:
            for i in re.findall('\([^()]\)', user_inp):
                user_inp = user_inp.replace(i, cal(i.replace('(', '').replace(')', '')))

while True:
    print(main(('0+'+input('>>>').replace(' ', ''))))



