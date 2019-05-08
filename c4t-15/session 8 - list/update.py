items = ['Baseball', 'Sleep', 'Voz']
items.append('Oranges')

# items[0] = 'Forrest Gump'
# print(items)

# items[-1] = input("Enter Favorite Book: ")
# print(*items, sep=" | ")

replace = int(input("Enter Number of Element: "))
items[replace-1] = input("Enter New Element: ")
print (*items, sep = ", ")