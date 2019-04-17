# for i in range (3, 13, 1):
#     print (i)

# end_number = input ("Enter End Number Here: ")
# for i in range (0, int(end_number) + 1, 1):
#     print (i)



# 0 to n odd ver.1
# start_number = input ("Enter Start Number Here: ")

# if int(start_number)%2!=0:
#     for i in range (int(start_number), -1, -2):
#         print (i)
# else:
#     for i in range (int(start_number)-1, -1, -2):
#         print (i)


# 0 to n odd ver.2
# start_number = int(input ("Enter Start Number Here: "))
# while True:
#     if start_number % 2 != 0:
#         print(start_number)
#         start_number -=2 
#         if start_number < 1:
#             break
#         # if  start_number == 1:
#         #     print (start_number)     
#         #     break  
#         # else:
#         #     print ("Sequence Over")
#         #     break
#     else:
#         # c = start_number - 1
#         # c +=-2
#         # if  c >= 0:
#         #     print (c)
#         # else:
#         #     print ("Sequence Over")
#         #     break
#         print(start_number)
#         start_number -=2 
#         if start_number < 0:
#             break



# TURTLEEEEEEEE
from turtle import *
side = int(input ("Enter Number of Side here: "))
for i in range (side):
    fd (100)
    rt (360/side)

mainloop()
