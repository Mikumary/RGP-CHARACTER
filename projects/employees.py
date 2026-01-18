"""Write a Python program that does the following:

Create a dictionary named employee with the following information:

"name" → employee’s name (string)

"age" → employee’s age (integer)

"salary" → employee’s salary (float)

Create a list of skills the employee has.

Add one more skill to the list.

Store the employee’s ID and year of joining inside a tuple.

Create a set of project codes the employee has worked on and add a new project code.

Print:

The employee’s full information (dictionary, list, tuple, and set)

The total number of skills the employee has."""

#dictionary
employee={"names":"mary",
          "age":56,
          "salary":800.7}
#list
skills=["java","html","css","python"]
print(skills)
skills.append("jungle")
print(skills)
#tuple
details=("id","year")
print(details)
#set
codes={56,67,87,93,45,90}
print(codes)
codes.add(765)
print(codes)
for x in range(len(skills)):
    print(f"{x} {skills[x]}")
#total skills
print("totalskills:",len(skills))

"""Write a Python program that does the following:

Ask the user to enter:

Student’s name

Age

Course name

Admission number

Store the information in a dictionary named student.

Create a list named subjects and let the user enter 3 subjects (one by one).

Add a fourth subject of your choice to the list.

Create a tuple containing the admission number and year of admission.

Create a set of 3 unique clubs or activities the student has joined and add one more.

Print:

The full student information

All subjects

The total number of subjects

The tuple (admission number, year)

The set of clubs"""

name=input("enter your name:")
age=input("enter your age: ")
coursename=input("enter your coursename")
admission=input("enter your adminission number:")
#dictionary
student={"name":name,
         "age":age,
         "coursename":coursename,
         "admission":admission}
print("student details:",student)
#list
kiswahili=input("enter subject kiswahili:")
english=input("enter your subject english:")
math=input("enter your language math: ")
subjects=[kiswahili,english,math]
print(subjects)
subjects.insert(-1,"social")
print("your subjects are:",subjects)
#tuple
yearadm=(447373,2009)
print("admission number and year:",yearadm)
#set
activities={"dancing","singing","drama"}
print("activities done:",activities)
activities.add("coding")
print(activities)
