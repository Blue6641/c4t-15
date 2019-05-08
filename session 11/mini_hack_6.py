dict1 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}
dict1["TOSHIBA"] = 5
dict1['FUJITSU'] = 15
dict1['ALIENWARE'] = 5
dict1["DELL"] = int(dict1["DELL"]) + 10
dict1["MACBOOK"] = 2


dict2 = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    # "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000,
}
sum1 = []
for i in dict1:
    for y in dict2:
        if i == y:
            print ("Total Price of", i, ":", dict1[i]*dict2[i])
            a=dict1[i]*dict2[i]
            sum1.append(a)
print("Total Value: ", sum(sum1))
        