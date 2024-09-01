customer = {
    'name': 'Juan',
    'lastname': 'Gómez',
    'birthday': {
        'month': 4,
        'day': 12,
        'year': 1993
        },
    'age': 2024 - 1993,
    'active': True
}

print(customer)
# >> {'name': 'Juan', 'lastname': 'Gómez', 'birthday': {'month': 4, 'day': 12, 'year': 1993}, 'age': 31}
print(customer['name'])
# >> Juan
print(customer['birthday']['year'])
# >> 1993
print(customer['age'])
# >> 31
print(customer['active'])
# >> True

dic = {'c1':'a', 'c2':'b'}
print(dic)
#>> {'c1': 'a', 'c2': 'b'}
dic['c2'] = 'B'
print(dic)
#>> {'c1': 'a', 'c2': 'B'}
dic[2] = 'C'
print(dic)
#>> {'c1': 'a', 'c2': 'B', 2: 'C'}

print(f"keys: {customer.keys()}")
#>>
print(f"values: {customer.values()}")
#>>
print(f"items: {customer.items()}")
#>>