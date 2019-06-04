def person(name, age, aggr, sex):
    person = {
        'name': name,
        'age': age,
        'aggr': aggr,
        'sex': sex
    }
    return person

ls = person('ls', 27, 1000, '男')
print(ls)