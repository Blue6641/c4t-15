# dict2 = {
#     "HP" : 600,
#     "DELL" : 650,
#     "MACBOOK" : 12000,
#     "ASUS" : 400,
#     "ACER" : 350,
#     "TOSHIBA" : 600,
#     "FUJITSU" : 900,
#     "ALIENWARE" : 1000,
# }

# name = input("Enter Brand Name: ")
# number = int(input("Enter Number of Purchase: "))

# print(dict2[name]*number)


dict1 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}
dict1['FUJITSU'] = 15
dict1['ALIENWARE'] = 5
dict1["DELL"] = int(dict1["DELL"]) + 10
dict1["MACBOOK"] = 2
dict1["TOSHIBA"] = 5

key = input("Enter Brand Name: ")
value = int(input("Enter Number of Purchase: "))
dict1[key] = dict1[key]-value

for i in dict1:
    print(i, ":", dict1[i])