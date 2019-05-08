# y = input("Enter Number Here: ")
# x = input("Enter SO CHIA Here: ")
# for i in range(0, int(y)+1):
#     if int(y) % x == 0:
#         n = (0 + int(y))*(((int(y)-)/2)+1)/2
#     else:
#         n = (1 + int(y))*(((int(y)-x-1)/2)+1)/2
# print (n)

# 1 2 3 4 5
n = int(input ("Enter Number Here: "))
sum = 0
for i in range (n+1):
    if i % 2 == 0:
        print ("i: ",i)
        sum += i # sum = sum + i

        print ("sum: ",sum)