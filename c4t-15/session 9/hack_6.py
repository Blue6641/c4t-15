area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
pipol = [150300, 247100, 333300, 266800, 420900, 318000]

############################################################
counter = -1
result = []
for _ in area:
    counter += 1
    ar = int(area[counter])
    pi = int(pipol[counter])
    re = pi/ar
    result.append(re)
print(*result, sep=', ')
############################################################


TB = sum(result)/len(area)
print("Average Population: ", TB)

