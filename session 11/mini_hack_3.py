from pprint import pprint
dict1 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}

# sum1 = sum(dict1.values())
# print(sum1)

dict1['FUJITSU'] = 15
dict1['ALIENWARE'] = 5
sum1 = sum(dict1.values())
print (sum1)

for i in dict1:
    print (i, ":", dict1[i])