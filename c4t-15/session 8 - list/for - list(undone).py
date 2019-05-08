items = ['Baseball', 'Sleep', 'Voz', 'Oranges', 'Milk', 'Cycling']

# for i in range (len(items)):
#     print(items[i].upper())

# for i, item in enumerate(items):
    # print(i+1, '.',  item.upper())
    # print(item.partition("e"))


for item in items: 
    if "e" in item:
        print (item)
    elif "E" in item:
        print (item)
    else:
        print ("Doesn't Contain 'E'")


# a = input("Letter: ")
# for item in items:
#     if a in item:
#         print(item)