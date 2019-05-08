# n = int(input ("Enter Month: "))

# if n < 4:
#     print ("Spring")
# elif 4 <= n < 6:
#     print ("Fall")
# elif 6 <= n < 9:
#     print ("Autumn")
# else:
#     print ("Winter")

import random 
number = random.randint(0, 100)
print (type(number))
print (number)

if number < 30:
    print("Rainy")
elif 30 < number < 60:
    print("Cloudy")
else:
    print("Sunny")