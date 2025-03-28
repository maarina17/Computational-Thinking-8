#Beginng: create variables
english_points = 0
history_points = 0

#Middle: ask questions
answer = input ("Would you rather A) learn, or B) teach?")
if answer == "A":
    history_points += 1
elif answer == "B":
    english_points +=1

answer = input ("Do you like A) yellow, or B) red?")
if answer == "A":
    english_points += 1
elif answer == "B":
    history_points +=1

answer = input ("Do you like A) writing, or B) typing?")
if answer == "A":
    english_points += 1
elif answer == "B":
    history_points +=1

answer = input ("Do you like A) fruits, or B) vegetables?")
if answer == "A":
    english_points += 1
elif answer == "B":
    history_points +=1

answer = input ("Do you like A) jackets, or B) hoodies?")
if answer == "A":
    english_points += 1
elif answer == "B":
    history_points +=1

#End: determine results
if english_points > history_points:
    print("You are english!")
elif english_points < history_points:
    print("You are history!")
