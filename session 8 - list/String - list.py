# Prob. 1

# items = []

# while True:
#     new_item = str(input("Enter New Item, or Break if End: "))
    
#     if new_item != "Break":
#         items.append(new_item)
#         print (*items, sep=", ")
#     else:
#         break

# new_elements = input("Enter New Elements: ")
# items.extend(new_elements)
# print(*items, sep = ", ")




# Prob.2

# from random import shuffle
# word = input("Enter a Word: ")
# word = list(word)
# shuffle(word)
# print(word)




# Prob. 3

items = ['Baseball', 'Sleep', 'Voz', 'Oranges', 'Milk', 'Cycling']
import random
score = 0
while True:
    RanItem=items[random.randint(0, 4)]
# print(RanItem)

    RanItem_1=list(RanItem)
    random.shuffle(RanItem_1)
    print(RanItem_1)
    

    answer = input("Rearrange the characters: ")
    if answer == RanItem:
        print ("Correct!")
        score +=1
        print ("Your Score: ", score)
    else:
        print ("Incorrect!")
        score -=1
        print (score)

