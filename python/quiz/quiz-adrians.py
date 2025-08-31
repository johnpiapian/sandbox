# Keep adding answers into the right_answers list as you make more questions
right_answers = ["20", "July 9", "Manuntag", "Diet Coke or Coke Zero", "e. bad girls", "a. Miraculous Ladybug", "d. not living up to my potential", "Wrong Quiz", "b. Larize", "Everything but yes" ]
your_answers= []

def final_score(name ,score, right_answers, your_answers):
    print()
    print()
    score_fin = str(score)
    if score < 0 or score == 0:
        print("you got "+ score_fin + " points " + name )
        print()
        print("wtf you got almost all, if not all of them wrong.")
    elif score > 0 and score < 6:
        print("you got "+ score_fin + " points " + name )
        print()
        print("Hello stranger")
    elif score >= 6 and score <= 10:
        print("you got "+ score_fin + " points " + name )
        print()
        print("We're okay friends")
    else :
        print("you got "+ score_fin + " points " + name )
        print()
        print("I love you. Marry me Already. We'll have 3 kids, a dog, and a hamster.")
    print()
    print("Lastly, here is to compare your answers to the right answers.")
    print()
    # Here you want to iterate over 2 lists and display the right answer and the user answer together.
    for r,y in zip((right_answers), (your_answers)):
        print("Right Answer:",[r],  "| Your answer:", [y])


# Do you want to play the game? If yes, continue, if no, print(Have a good day")
total_score = 0
    
print("This is the how well do you know Adrian game.")

print()
    
answer_1 = input("Do you dare to play? (yes or no) ")
x = answer_1.lower()
if x == "yes":
    print()
    print("Let's continue.")
    print()
    answer_name = input("What will be your name? ")
    print("Hello " + answer_name)
    print()
    print()
    

elif x != "yes":
    print("Have a good day.")
    quit()#quits the program



ques_1 = input("Question 1: How old is Adrian? ")
your_answers.append(ques_1)
if ques_1 == "20":
    print("Good Job")
    total_score += 1
else:
    print("Incorrect")


print()
print()


ques_2 = input("Question 2: When is my Birthday? ").lower()
your_answers.append(ques_2)
if ques_2 == "july 9":
    print("Wow can't believe you got that")
    total_score += 1
else:
    print("dumbass, you got it wrong. Just for that you get -1 point")
    total_score -= 1

print()
print()

ques_3 = input("Question 3: Can you spell my last name? ").lower()
your_answers.append(ques_3)
if ques_3 == "manuntag":
    print("you're a genius")
    total_score += 1
    
else:
    print("I'm disappointed")

print()
print()

ques_4 = input("Question 4: What is my favorite soda? ").lower()
your_answers.append(ques_4)
if ques_4 == "diet coke" or ques_4 == "coke zero":
    print("you're a God. For that I will double your score")
    total_score *= 2
    
else:
    print("This was a tough one, I'm not even be mad that you missed it.")

print()
print()

ques_5 = input("Question 5: What is my racial preference?\n a. White\n b. Black\n c. Asian\n d. Mexican\n e. bad girls\n ").lower()
your_answers.append(ques_5)
if ques_5 == "bad girls" or ques_5 == "e" or ques_5 == "e.":
    print("I'm gonna cry that you got this right. You get 2 points")
    total_score += 2
elif ques_5 == "asian" or ques_5 == "c" or ques_5 == "c.":
    print("Not quite right but I'll give you a half point")
    total_score += 0.5
    
else:
    print("*sigh* on to the next question")

print()
print()

ques_6 = input("Question 6: Which is my favorite show?\n a. Miraculous Ladybug\n b. Wednesday\n c. The Office\n d. squid games\n ").lower()
your_answers.append(ques_6)
if ques_6 == "miraculous ladybug" or ques_6 == "a" or ques_6 == "a.":
    print("Just shut up and kiss me already")
    total_score += 1

else:
    print("I'm gonna punch you for getting that wrong")
    total_score -= 1

print()
print()

ques_7 = input("Question 7: What is a big fear of mine?\n a. Heights\n b. Failure \n c. Being Lonely \n d. Not living up to my potential\n ").lower()
your_answers.append(ques_7)
if ques_7 == "not living up to my potential" or ques_7 == "d" or ques_7 == "d.":
    print("I think I'm in love")
    total_score += 1

else:
    print("(T_T)")

print()
print()    

ques_8 = input("Question 8: What do I notice first in a girl\n a. Face \n b. body \n c. style \n d. personality\n ").lower()
your_answers.append(ques_8)
if ques_8 == "face" or ques_8 == "a" or ques_8 == "a.":
    print("You're beautiful")
    total_score += 1

else:
    print(" (T w T)")
    print("Why do you hate me?")   
    
print()
print()

ques_9 = input("Question 9: God gives me a gun. He tells me to shoot one of the following people or I go to hell, who is dying?\n a. Juliana\n b. Larize\n c. Nerissa\n d. Joey\n").lower()
your_answers.append(ques_9)
if ques_9 == "larize" or ques_9 == "b" or ques_9 == "b.":
    print("Some people just gotta make the tough decisions in life")
    total_score += 1
elif ques_9 == "juliana" or ques_9 == "a" or ques_9 == "a.":
    print("🤨🙃")
    total_score /= 2

else:
    print("Wrong person.")
    total_score -= 1
    
print()
print()

ques_10 = input("Question 10: Am I sexy?\n a. Yes \n b.YES!! \n c. YES DADDY \n d. si papi\n ").lower()
your_answers.append(ques_10)
if ques_10 == "yes!!" or ques_10 == "yes daddy" or ques_10 == "si papi" or ques_10 == "b" or ques_10 == "c" or ques_10 == "d" or ques_10 == "b." or ques_10 == "c." or ques_10 == "d.":
    print("I'm charmed")
    total_score += 1

else:
    print("Wow you're bad, but not the good bad")
    total_score = 0






final_score(answer_name , total_score, right_answers, your_answers)


        

    


    




    


        

    
        

