name = ["Huy", "Tung", "Duc"]
role = ["Waiter", "Cook", "Manager"]
hours = [12, 24, 20]
salary = [0.8, 1.5, 2.0]

table = {
    'Name' : ["Huy", "Tung", "Duc"],
    'Role' : ["Waiter", "Cook", "Manager"],
    'Hours' : [12, 24, 20],
    'Salary' : [0.8, 1.5, 2.0]
}

new_name = ["Don", "H.Duc"]
new_role = ['Waiter', "Waiter"]
new_hours = [12, 14]
new_salary = [0.9, 0.7]
counter = 0
for i in range (2):
    name.append(new_name[i])
for i in range (2):
    hours.append(new_hours[i])
for i in range (2):
    salary.append(new_salary[i])
for i in range (2):
    role.append(new_role[i])

table["Name"] = name
table['Role'] = role
table['Salary'] = salary
table["Hours"] = hours
    


print(table)