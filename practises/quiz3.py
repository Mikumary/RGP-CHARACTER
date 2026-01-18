"""    1. Create a dictionary with 3 contacts (name → phone number) and print each contact.
    2. Update a phone number in the dictionary.
    3. Create a set of numbers and add a new number.
    4. Find common elements between two sets.
"""

classmates={
"mate1":{
"name": "mary",
"phone": 7431289},

 "mate2":{
    "name":"nick",
    "phoneno": 737822
 },
 "mate3":{
     "name":"colins",
     "phoneno":947392
 }

}
print(classmates)
#updating a phonenumber
classmates["mate2"].update({"phoneno":7896532})
print(classmates)
for x, obj in classmates.items():
    print(x)
    for y in obj:
        print(y+ ":", obj[y])
        #sets
num1={1,2,3,4,5}
num1.add(6)
print(type(num1))
print(num1)
num2={1,5,6,4,6,8}
y=num1.intersection(num2)
print(y)



