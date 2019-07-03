import requests

import re
import json


def getPage(url):
    response = requests.get(url)
    return response.text


def parsePage(s):
    com = re.compile(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
        '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)

    ret = com.finditer(s)
    for i in ret:
        yield {
            "id": i.group("id"),
            "title": i.group("title"),
            "rating_num": i.group("rating_num"),
            "comment_num": i.group("comment_num"),
        }


def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    response_html = getPage(url)
    ret = parsePage(response_html)
    print(ret)
    f = open("move_info7", "a", encoding="utf8")

    for obj in ret:
        print(obj)
        data = json.dumps(obj, ensure_ascii=False)
        f.write(data + "\n")


if __name__ == '__main__':
    count = 0
    for i in range(10):
        main(count)
        count += 25

'''
flags有很多可选值：

re.I(IGNORECASE)忽略大小写，括号内是完整的写法
re.M(MULTILINE)多行模式，改变^和$的行为
re.S(DOTALL)点可以匹配任意字符，包括换行符
re.L(LOCALE)做本地化识别的匹配，表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境，不推荐使用
re.U(UNICODE) 使用\w \W \s \S \d \D使用取决于unicode定义的字符属性。在python3中默认使用该flag
re.X(VERBOSE)冗长模式，该模式下pattern字符串可以是多行的，忽略空白字符，并可以添加注释
'''

'''
url从网页上把代码爬取下来
bytes decode --》 utf-8 网页内容就是我待匹配的字符串
ret = re.findall(正则，待匹配的字符串)  ret是所有匹配到的内容组成的列表
'''


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

a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
a = a.strip('')
print(a)