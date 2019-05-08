table = [
    {
        'name' : 'Huy',
        'role' : 'Waiter',
        'hours' : '12',
        'salary' : '0.8',
    },
    {
        'name' : 'Tung',
        'role' : 'Cook',
        'hours' : '24',
        'salary' : '1.5',
    },
    {
        'name' : 'M.Duc',
        'role' : 'Manager',
        'hours' : '20',
        'salary' : '2',
    }
]

month = []
for i in range (3):
    month_sal = float(table[i]['hours'])*float(table[i]['salary'])*30
    month.append(month_sal)
print(month)

x = sum(month)
print (x)