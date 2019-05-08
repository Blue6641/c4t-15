###################################################

lst = [5, 1, 8, 92, 7, 30]
a = -1
num = lst[a]
lst_even = []
for i in range(len(lst)):
    a +=1 
    num = lst[a]
    if num % 2 == 0:
        lst_even.append(num)
    print(num)

print(lst_even)

#####################################################


new_lst = input ("Enter a List of Numbers, Seperated by ',': ")
lst = new_lst.split(", ")
print(lst)
# print(type(lst[1]))

a = -1
num = int(lst[a])
lst_even = []
for i in range(len(lst)):
    a +=1 
    num = int(lst[a])
    if num % 2 == 0:
        lst_even.append(num)
    print(num)

print(lst_even)


