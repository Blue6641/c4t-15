from turtle import *
# color('purple')
# shape("turtle")
# speed(-1)
# right (45)
# for i in range (300):
#     for i in range (4):
#         forward(100)
#         left(90)
#     left (7)

# right (45)
# mainloop()

# n = input("Enter number of side")

shape ("turtle")
for i in range (3, 20):
    for _ in range (i):
        color ("blue")
        fd (100)
        lt (360 / int(i))

mainloop()