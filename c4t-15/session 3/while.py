# Validate Name
# while True:
#     txt = input ("Enter Name: ")
#     if txt.isdigit():
#         print ("Not a Name")
#     else:
#         print (txt)
#         break

# Validate Password (1)
# while True:
#     password = input ("Enter Password: ")
#     if password.isalpha():
#         print ("Invalid Password")
#     else:
#         print ("Ok")
#         break

# Validate Password (2)
while True:
    password = input("Enter Password: ")
    if password.isalpha():
        print("Invalid Password")
    elif len(password) < 8:
        print("Password must contain 8 digits/characters")
        break
    else:
        print("OK")
        break

        