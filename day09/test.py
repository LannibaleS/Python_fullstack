# a = 707829217
# b = 14
# for i in range(1,707829218):
#     # print(i)
#     c = 707829217/i
#     print(c, i, isinstance(c, int))
    # d = isinstance(c, int)
    # print(isinstance(c, int))
    # if isinstance(c, int):
    #     print('int')
    #     print(c, i)

import math
from math import sqrt

for i in range(2, int(sqrt(707829217) + 1)):
    # print(i)
    if 707829217 % i == 0: print(i, 707829217 / i)

import re
b = 866278171
d = 33
c = 0
for i in range(80000000+1):
    if i % 2 == 1:
        i = str(i)
        # print(i, type(i))
        for j in i:
            # print(j)
            if j == '3':
                c += 1
        # m = re.findall(r'(\w*[3]+)\w*', i)
        # print(m)
        # print(i.split(','))
        # print(''.join(i))
print('c',c)
# li = '13'
# for i in li:
#     print(i)