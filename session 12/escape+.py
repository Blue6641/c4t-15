#SETUP

import random
inventory = []
while True:
    map_size = {
        'map_x' : 6,
        'map_y' : 6
    }
    P = {
        'x' : random.randint(0,5),
        'y' : random.randint(0,5)
    }
    K = {
        'x' : random.randint(0,5),
        'y' : random.randint(0,5)
    }
    E = {
        'x' : random.randint(0,5),
        'y' : random.randint(0,5)
    }
    W = {
        'x' : random.randint(0,5),
        'y' : random.randint(0,5)
    }
    if (P["x"] != K["x"] and P["y"] != K["y"]):
        if (P["x"] != E["x"] and P["y"] != E["y"]):
            if(E["x"] != K["x"] and E["y"] != K["y"]):
                if (W["x"] != K["x"] and W["y"] != K["y"]) and (W["x"] != P["x"] and W["y"] != P["y"]) and (W["x"] != E["x"] and W["y"] != E["y"]):
                    break
    

def printmap ():
    for y in range(map_size['map_y']):
        for x in range(map_size['map_x']):
            if y == P['y'] and x == P['x']:
                print("P",end=" ")
            elif y == K['y'] and x == K['x']:
                print("K",end=" ")
            elif y == E['y'] and x == E['x']:
                print("E",end=" ")
            elif y == W['y'] and x == W['x']:
                print("W",end=" ")
            else:
                print("_",end=" ")
        print()
    return


def movement():
    if act == "up":
        P["y"] = P["y"]-1
    elif act == "down":
        P["y"] = P["y"]+1
    elif act == "left":
        P["x"] = P["x"]-1
    elif act == "right":
        P["x"] = P["x"]+1
    if (P["y"] >= 0 and P['y'] <= map_size['map_y']-1) and (P["x"] >= 0 and P['x'] <= map_size['map_x']-1):
        if (W["x"] != P["x"] or W["y"] != P["y"]):
            printmap()
    return

def mapcheck():
    if P["y"] < 0 or P['y'] > map_size['map_y']-1:
        print ("Hit Wall")
        if act == "down":
            P["y"] = 5
            printmap()
        elif act == "up":
            P["y"] = 0
            printmap()
    elif P["x"] < 0 or P['x'] > map_size['map_x']-1:
        print ("Hit Wall")
        if act == "right":
            P["x"] = 5
            printmap()
        elif act == "left":
            P["x"] = 0
            printmap()
    if (W["x"] == P["x"] and W["y"] == P["y"]):
        print("Hit Wall")
        if act == "right":
            P['x']=W["x"]-1
            printmap()
        if act == "left":
            P['x']=W["x"]+1
            printmap()
        if act == "up":
            P['y']=W["y"]+1
            printmap()
        if act == "down":
            P['y']=W["y"]-1
            printmap()
    return



def eval():
    if P["x"] == K["x"] and P["y"] == K["y"]:
        K['x'] = -1
        K['y'] = -1
        inventory.append("key")
    return


#RUNGAME

printmap()
while True:
    act = str(input("Your move?"))
    movement()
    mapcheck()
    eval()
    if P["x"] == E["x"] and P["y"] == E["y"]:
        if "key" in inventory:
            print("Endgame")
            break
        else:
            print ("You Need Key")

    

    