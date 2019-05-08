char = {
    'Name' : 'Light',
    'Age' : 17,
    'Strength' : 8,
    'Defence' : 10,
    'HP' : 100,
    'Backpack' : ["Shield", "Bread Loaf"],
    'Gold' : 100,
    'Level' : 2,
}


char['Gold'] = char['Gold']+50
char['Backpack'].append("Flintstone")
print (char['Backpack'])
char['Pocket'] = ["MonsterDex", "Flashlight"]
for i in char:
    print (i, ":", char[i])