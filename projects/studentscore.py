"""Write a Python program that does the following:
Create a list of student scores (for example: [78, 56, 89, 90, 67, 45, 99]).
Use a for loop to print each score.
Find and print:
The highest score
The lowest score
The average score
Finally, use a loop to print:
"Pass" if the score is 50 or above
"Fail" if it’s below 50"""
studentscore=[78,56,59,89,90,67,45,99]
#looping in each score
for i in studentscore:
    print(i)

    #the highest score 
highestscore=max(studentscore)
print(f"highest score is {highestscore}")

#lowest score
lowestscore=min(studentscore)
print(f"the lowest score is {lowestscore}")

#average score
averagescore=sum(studentscore)/len(studentscore)
print(f"the average score is {averagescore}")

#checking if the score is above or below 50
for score in studentscore:
 if score>=50:
    print(score,"pass")
 else:
    print(score,"fail")


