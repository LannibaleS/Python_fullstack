dic = {
    'name':['alex','wusir','taibai'],
    'py9':{
        'time':'1213',
        'learn_money':19800,
        'addr':'CBD',
           },
    'age':21
}

dic['age'] = 56
print(dic)

dic['name'].append('ls')
print(dic['name'])

dic['py9']['name'] = 'ls'
print(dic['py9'])


info = input('>>>').strip()
for i in info:
    if i.isalpha():
        info = info.replace(i, ' ')
# print(info)
l = info.split()
print(len(l))
