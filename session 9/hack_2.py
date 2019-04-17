# col = ["Burgundy", "Grey", "Purple", "Blue"]

# print("The Colors Are: ") 
# print(*col, sep=", ")

# col_no = int(input("Enter Color Number: "))
# print("The Color is:", col[col_no-1])




##########################################################################
# while True:
#     col = ["Burgundy", "Orange", "Purple", "Blue"]
#     for i, item in enumerate(col):
#         print(i+1, '.', item)
#     delete_str = input("Enter Color to Delete: ")
#     col.remove(delete_str)
#     for i, item in enumerate(col):
#         print(i+1,'.', item)
#     print("New Cycle") 
#     col_2 = ["Burgundy", "Orange", "Purple", "Blue"]
#     for x, color in enumerate(col_2):
#         print(x+1, '.', color)
#     delete_int = int(input("Enter Number of Color to Delete: "))
#     col_2.pop(delete_int-1)
#     for x, color in enumerate(col_2):
#         print(x+1, '.', color)
#         break
    # DIS IS WRONGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
# ###########################################################






# col = ["Burgundy", "Orange", "Purple", "Blue"]
# for i, item in enumerate(col):
#         print (i+1, ".", item)
# answer = input("Item to Delete: ")
# while True:
#     if answer.isdigit():
#         answer = int(answer)
#         col.pop(answer-1)
#         for i, item in enumerate(col):
#             print (i+1, ".", item)
#             # if i+1 > len(col):
#             #     print("invalid input")
#     else:
#         answer = str(answer)
#         col.remove(answer)
#         for i, item in enumerate(col):
#             print (i+1, ".", item)
#     # elif answer.isdigit():
#     #     if int(answer+1) > len(col):
#     #         print("invalid input")
#         break



########################################################################



from turtle import *
col = ["Burgundy", "Orange", "Purple", "Blue"]
i = 0
for i in range(3):
    i += 1
    color(col[i])
    forward(100)

mainloop()