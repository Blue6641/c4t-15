items = ['Baseball', 'Sleep', 'Voz', 'Milk']
print (items)

while True:
    action = str(input("Choose Action (Create, Read, Update, Delete): "))

    if action == "Create":
        items.append(input("Add Item to End of List: "))
        print (*items, sep = ', ')
        
    
    if action == "Read":
        for item in items:
            print (*items, sep = ', ')
            
        if items == []:
            print ("No Element in List")
            
    
    if action == "Update":
        replace = int(input("Enter Number of Element: "))
        items[replace-1] = input("Enter New Element: ")
        print (*items, sep = ", ")
        

    if action == "Delete":
        i = int(input("Enter No. of Item to Delete: "))
        items.pop(i-1)
        print(*items, sep=", ")

        
