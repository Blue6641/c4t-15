# MATHFREAK



# print ("1 + 1 = 2")
# answer = str(input("Your Answer(True or False): "))
# # while True:
# if answer == "True" or answer == "true" or answer == "T" or answer == "t":
#     print ("Correct!")
#     print ("1 + 1 = 3")
#     answer2 = str(input("Your Answer(True or False): "))
#     if answer2 == "True" or answer2 == "true" or answer2 == "T" or answer2 == "t":
#         print("Incorrect! You lose!") 
#     else:
#         if answer2 == "False" or answer2 == "false" or answer2 == "F" or answer2 == "f":
#             print ("Correct!")
#         else:
#             print ("Incorrect!")
# else:
#     if answer == "False" or answer == "false" or answer == "F" or answer == "f":
#         print ("Incorrect!")     
#     else:
#         print("End game") 



import random
score = 0
while True:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    # c = random.randint(0, 20)
    d = random.randint(-10, 10)
    print(a, "+", b,"=", a+b+d)
    answer = str(input("Your Answer(True or False): "))
    if d == 0:
        if answer == "True" or answer == "true" or answer == "T" or answer == "t":
            print ("Correct!")
            score += 1
            print("Your score is now: ", score)
        else:
            if answer == "False" or answer == "false" or answer == "F" or answer == "f":
                print ("You lose!")
                print("Your score is: ", score)
                break
            else:
                print ("Invalid Answer!")
            
    elif d != 0:
        if answer == "False" or answer == "false" or answer == "F" or answer == "f":
            print ("Correct!")
            score += 1
            print("Your score is now: ", score)
        else:
            if answer == "True" or answer == "true" or answer == "T" or answer == "t":    
                print ("You Lose!")
                print("Your score is: ", score)
                break
            else:
                print ("Invalid Answer!")
    else:
        print ("End Game!")
        break

        