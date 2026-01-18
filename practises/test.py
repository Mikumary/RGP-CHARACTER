#input name 
name=input("enter your name: ")
age=int(input("enter your age: "))
info=f"hello {name} you are {age} years old"
print (info)
#math operation
num=float(input("input the first number: "))
Num=float(input("input the second number: "))
sum1=num+Num
product=num*Num
diff=num-Num
que=num/Num
print(sum1)
print(product)
print(diff)
print(que)
#checking the numbers
x=int(input("input any number:"))
if x%2==0:
    print(f"{x} is an even number")
else:
    print(f"{x}is an odd number")
#dictionaries
thisdict=dict(name="mary",age=20,year=2005,gender="f")
x=thisdict["age"]
print(f"she is {x} years old")
y=thisdict.items()
print(y)
year=2025
print(y)
thisdict.update({"month":3})
print(y)
    



