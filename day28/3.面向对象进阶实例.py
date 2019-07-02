
from  collections import namedtuple
Card = namedtuple('Card', ['rank', 'suit'])

import json

class FranchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = ['红心','方板','梅花','黑桃']

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in FranchDeck.ranks
                                        for suit in FranchDeck.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __str__(self):
        return json.dumps(self._cards, ensure_ascii=False)

deck = FranchDeck()
print(deck[0])

from random import choice
print(choice(deck))
print(choice(deck))

from random import  shuffle
shuffle(deck)
print(deck[0])
print(deck)

print(deck[:5])


print('\n=====一道面试题：100个人去重，名字，性别一样，年龄不一样===')
'''
一道面试题：100个人去重，名字，性别一样，年龄不一样
'''
class A:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
        return False

    def __hash__(self):
        return hash(self.name + self.sex)

a = A('ls', 'male', '26')
b = A('ls', 'male', '27')
c = (a,b)
print(c)
print(set(c))