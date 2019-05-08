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

# print(table[2]['salary'])




# p1 = {
#     'name' : 'Huyen',
#     'role' : 'Waitress',
#     'hours' : 14,
#     'salary' : 1
# }

# table[0] = p1
# print(table[0])




# table.pop(2)
# print(table)



# print(*table, sep = "\n")


month = []
for i in range (3):
    month_sal = float(table[i]['hours'])*float(table[i]['salary'])*30
    month.append(month_sal)
print(month)