import random
skllset = {
    'Skill 1' : {'Name':'Tackle','Minimum level':1,'Damage':5,'Hit rate':0.3,},
    'Skill 2' : {'Name':'Quick Attack','Minimum level':2,'Damage':3,'Hit rate':0.5},
    'Skill 3' : {'Name':'Strong Kick','Minimun level':4,'Damage':9,'Hit rate':0.2} 
}

level = input ("Enter Skill Level: ")
for key, value in skllset.items():
    print (key, "-", value)

action = input ("Enter Skill Number: ")

if int(action) == 1:
    for k, val in skllset['Skill 1'].items():
        if int(level) < 1:
            print ("Unusable!")
        else:
            if k == 'Hit rate':
                ran = random.uniform(0, 1)
                if ran < val:
                    print("Unexecuted!")
                else: 
                    for key, value in skllset['Skill 1'].items():
                        if key == 'Damage':
                            print ('Your Damage is: ', value)

if int(action) == 2:
    for k, val in skllset['Skill 2'].items():
        if int(level) < 2:
            print ("Unusable!")
        else:
            if k == 'Hit rate':
                ran = random.uniform(0, 1)
                if ran < val:
                    print("Unexecuted!")
                else: 
                    for key, value in skllset['Skill 2'].items():
                        if key == 'Damage':
                            print ('Your Damage is: ', value)

if int(action) == 3:
    for k, val in skllset['Skill 3'].items():
        if int(level) < 4:
            print ("Unusable!")
        else:
            if k == 'Hit rate':
                ran = random.uniform(0, 1)
                if ran < val:
                    print("Unexecuted!")
                else:
                    for key, value in skllset['Skill 2'].items(): 
                        if key == 'Damage':
                            print ('Your Damage is: ', value)

