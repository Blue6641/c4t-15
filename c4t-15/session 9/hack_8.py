scr = [45, 67, 56, 78]
scr.sort(reverse=True)

################################################################
# print("High Scores:")
# for i, score in enumerate(scr):
#     print (i+1, ".", score)
# while True:
#     new_scr = int(input("Enter New High Score: "))
#     if new_scr != 0:
#         scr.append(new_scr)
#         scr.sort(reverse=True)
#         for i, score in enumerate(scr):
#             print (i+1, ".", score)
#     else:
#         print ("Didn't Make the List!")
#         break
################################################################

# 5 firsts
################################################################
print("High Scores:")
for i, score in enumerate(scr):
    print (i+1, ".", score)
while True:
    new_scr = int(input("Enter New High Score: "))
    if new_scr != 0:
        scr.append(new_scr)
        scr.sort(reverse=True)
        for i, score in enumerate(scr):
            print (i+1, ".", score)
            if i >= 4:
                break
    else:
        print ("Didn't Make the List!")
        break