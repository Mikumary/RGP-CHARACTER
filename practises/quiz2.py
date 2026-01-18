""" 1. Create a list of 5 fruits and print them one by one.
    2. Add a new fruit to the list and remove one.
    3. Create a tuple of 5 numbers and find the largest number.
    4. Slice the first 3 elements from a list."""
fruits=["apple","mango","pinaapple","melon","kiwi"]
for x in range(len(fruits)):
     print(fruits[x])
fruits.append("orange")
fruits.remove("kiwi")
print(fruits)
#fruits.pop([1:3])
print(fruits[0:3])
#tuples
num=(1,2,3,4,5)
maxi=max(num)
print(maxi)
print(type(num))

class employee:
    

     def __init__(self,fname ,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
     def fullname(self):
         return '{} {}'.format(self.fname,self.lname)
    
emp_1=employee("Mary","Miku",45)
emp_2=employee("Nick","Amedi",67)
        
print(emp_1.fullname())

