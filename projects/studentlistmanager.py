""" Write a Python program that does the following:
Create a list of student names (at least 5 names).
Print all the student names using a loop.
Ask the user to:
Add a new student name to the list.
Replace one existing name with another name.
Remove one student from the list.
Print the updated list after each change.
Finally:
Print the total number of students.
Print the first and last student in the list."""

names=["mary","nick","Collins","kelvin","Hikanote"]
 #printing the names
for name in names:
    print(name) 
#replacing one student 
print("----replacing kelvin with merlene---")
names[3]=("merlene")
print(names)
 #asking the user to add a new user to the list
student=input("Add a new student to the list:")
names.append(student)
names.insert(2,student)
print("---adding ann to the list at the beging at the end---")
print(names)
#removing one student from the list
print("----removed ann from the list---")
names.pop(2)
print(names)

#the total numbers of student 
print(len(names))
#the last and first student in the list
print("----printing the fast number in the list-----")
print(names[0])
print("-----printing the last number in the list----")
print(names[-1])
#sorting the names according to the case 
names.sort()
names.sort(key=str.lower)
print(f"sorted list{names}")