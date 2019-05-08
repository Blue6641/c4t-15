import random
import math
randlist = random.sample(range(0,3), 3)
print (randlist)
questions = ["Octopus' legs?", "Meaning of life?", "Iron Man?"]
quiz = [
    {
        "A" : "6",
        "B" : "7",
        "C" : "8",
        "D" : "9",
    },
    {
        "A" : "40",
        "B" : "42",
        "C" : "44",
        "D" : "46",
    },
    {
        "A" : "Chris Hemsworth",
        "B" : "Robert Downey Jr.",
        "C" : "Chris Pratt",
        "D" : "Chris Evans",
    }
]
a = 0
score = 0
while True:
    
    
    counter = randlist[a]
    a+=1
    print (questions[counter])
    print (quiz[counter])
    answer = str(input("Enter Your Answer Here: "))
    if counter == 0:
        if answer == "C":
            print("Correct!")
            score += 1
            print ("Your score is: ", score)
        else:
            print("Wrong!")
    elif counter == 1:
        if answer == "B":
            print("Correct!")
            score += 1
            print ("Your score is: ",score)
        else:
            print ("Wrong!")
    else:
        if answer == "B":
            print("Correct!")
            score += 1
            print ("Your score is: ", score)
        else:
            print ("Wrong!")
    if a == 3:
        # print ("Your score percentage: ", (score*100//len(questions)))
        score_percentage = score/len(questions)*100
        print("Your score is: ", round(score_percentage), "%")
        # print(score_percentage)
        break
