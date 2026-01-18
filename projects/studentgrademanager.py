"""Write a Python program that:

Asks the user to enter a student’s marks (0–100).

Uses an if–elif–else statement to determine the grade:

80–100 → Grade A

70–79 → Grade B

60–69 → Grade C

50–59 → Grade D

Below 50 → Grade F

Keeps asking for another mark until the user types "exit"."""
while True:
    grade=input("Enter students marks: ")
    if  grade.lower()=="exit":
        print("goodbye")
        break
    grade=int(grade)
    if grade>=80 and grade<=100:
        print("Grade: A")
    elif grade>=70 and grade<=79:
        print("Grade: B")
    elif grade>=60 and grade<=69:
        print("Grade: C")
    elif grade>=50 and grade<=59:
        print("Grade: D")
    else:
        print("Grade: F")

"""Write a Python program that:
Asks the user to enter a temperature in Celsius.
Converts it to Fahrenheit using the formula:
Fahrenheit = (Celsius * 9/5) + 32
Uses if–elif–else to categorize the weather based on Celsius:
Above 35 → "Very hot"
25–35 → "Hot"
15–24 → "Warm"
5–14 → "Cool"
Below 5 → "Cold"""

while True:
 temp=input("enter your temperature in celcius: ")
 if temp.lower()=="close":
     print("thank you, for your feedback")
     break
 try:
  temp=int(temp)
 except ValueError:
     print("please enter the correct value or type close")
     continue

 fahrenheit=(temp * 9/5) + 32
 print(f"Temperature in Fahrenheit: {fahrenheit}°F")
 if temp>=35:
     print("very hot ")
 elif temp>=25 and temp<=35:
     print("hot")     
 elif temp>=15 and temp<=24:
     print("warm")
 elif temp>=5 and temp<=14:
     print("cool")
 else:
     print("cold")


