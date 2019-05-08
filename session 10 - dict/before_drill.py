trout = {
    "name" : "Mike Trout",
    "number" : "27",
    "team" : "Los Angeles Angels of Anaheim",
    "description" : "Trout has been dubbed the greatest player of our generation. However, after signing the biggest extention contract ever to LAA, he isn't likely to win a WS anytime soon."
    }

trout["salary"] = "$426,500,000"

# key = input("Enter New Key: ")
# value = input("Enter New Value: ")
# trout[key] = value
print(trout)

# print(trout["name"])
# print(trout["salary"])

# key_print = input("Enter Key for Printing: ")
# print(trout[key_print])

# trout["description"] = "Trout has been dubbed the greatest player of our generation. However, after signing the biggest extention contract ever to LAA, he isn't likely to win a WS anytime soon. Unless Shohei Ohtani recovers, that is."
# key_change = input("Enter a Key: ")
# value_change = input("Enter new Value: ")
# trout[key_change] = value_change
# print(trout)

# del trout["description"]
# print(trout)

delete = input("Enter Key to Delete: ")
del trout[delete]
print (trout)