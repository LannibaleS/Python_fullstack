def demo():
    for i in range(4):
        yield i

g=demo()
print(g)
g1=(i for i in g)

print('g1:',g1)
print(list(g1))

g2=(i for i in g1)
print(list(g2))

''' 
生成器中的数据，只能取一次，取完就没有了
g1管g要值，只能要一次，要完就没数据了
g2管g1要，g1管g要，但是g已经没有值了，所以list[g2]是空列表
'''

def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test()          # i: 0,1,2,3
for n in [1,10]:  # n: 1,10
    g=(add(n,i) for i in g)

'''for 循环套生成器的题，把它拆开'''

n = 1
g=(add(n,i) for i in g)   # g=(add(n,i) for i in test())
n = 10
g=(add(n,i) for i in g)   # g=(add(n,i) for i in (add(n,i) for i in test()))

'''g=(add(10,i) for i in (add(10,i) for i in (0,1,2,3))
   g=(add(10,i) for i in (10,11,12,13))
   (20,21,22,23)


'''

print(list(g))

# [1,3,5,7,5,6,7,8,9]