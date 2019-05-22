skllset = {
    'Skill 1' : {'Name':'Tackle','Minimum level':1,'Damage':5,'Hit rate':0.3,},
    'Skill 2' : {'Name':'Quick Attack','Minimum level':2,'Damage':3,'Hit rate':0.5},
    'Skill 3' : {'Name':'Strong Kick','Minimun level':4,'Damage':9,'Hit rate':0.2} 
}
counter = 1
# for key,value in skllset.items():
for k, val in skllset['Skill 1'].items():
    if k == 'Name':
        print (counter, val)
        counter +=1

