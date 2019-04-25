

li = [
    { 'name':'apple', 'price':10},

    {'name': 'banana', 'price': 20},

    {'name': 'peach', 'price': 30},
]

shopping_cart = {}

print('welcome')
money = input('show me your money')
if money.isdigit() and int(money) > 0:
    for i,k in enumerate(li):
        print('序号{}, 商品{}, 价格{}'.format(i, k['name'], k['price']))

    choose = input('请输入商品序号')
    if choose.isdigit() and int(choose) < len(li):
        number = input('要购买的商品数量')
        if number.isdigit():
            if int(money) > li[int(choose)]['price'] * int(number):
                money = int(money) - li[int(choose)]['price'] * int(number)

                if li[int(choose)]['price'] in shopping_cart:
                    pass

            else:
                print('钱不够！回家跟你老婆要钱去')

