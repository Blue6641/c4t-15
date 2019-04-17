user = str(input("Enter User Name Here: "))
password = str(input("Enter Password Here: "))


while True:
    if len(password) > 8:
        print ("Correct!")
        break
    else: 
        print ("Incorrect! Password need to be at least 8 characters.")
        password = str(input("Enter Password Here: "))   
repass = str(input("Reenter Password: "))
while True:
    if repass != password:
        print ("Incorrect")
        repass = str(input("Reenter Password: "))
    else:
        print ("Correct") 
        break

email = str(input("Enter Email Here: "))
while True:
    if '@'  in email and '.com' in email:
        print ("Correct!")
        break
    else:
        print ("Incorrect! Not a valid email.")
        email = str(input("Enter Email Here: "))









