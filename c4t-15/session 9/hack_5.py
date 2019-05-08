name = ["SD", "BT", "BTL", "CG", "DT", "HBT"]
pipol = [150300, 247100, 333300, 266800, 420900, 318000]

print (max(pipol))
print (min(pipol))

print("Province with Most People: ", name[pipol.index(max(pipol))])
print("Province with Least People: ", name[pipol.index(min(pipol))])