#printing and comments
age=20
name="mary"
info=f"age {age}\nname {name}"
#printing name and age
print(info)
#concation
num=20
fruit="apple"
total=str (age)+ " " + fruit
print(total)
#asking the user to input two numbers
a=int(input("input the first number: "))
b=int(input("input the second number: "))
sum=a+b
print( "sum is"+" "+str(sum))
#creating a variable
color="pink"
print("my favourite color is"+" "+color)
print(type(color))
#list
fruits=["mary","cherry","mango","apple"]
print(fruits)
fruits.pop(2)
print(fruits)
fruits.remove("mary")
print (fruits)
def wordlength(w):
    return len(w)
mylist=["books","novels","magazines","new","enoch","bible"]
mylist.sort(key = wordlength)  
print(f"word lenght{mylist}")
#changing items
mylist[1]="God"
print(mylist)
mylist[2:6]=("Jesus","holyspirit")
print(mylist)
#inserting
mylist.insert(1,"God the father")
print(mylist)
#looping
for x in mylist:
    print(x)
#looping using an index 
for i in range(len(mylist)):
    print(f"item {mylist[i]} is in index {i}")

#while loop
r=0
while r < len(mylist):
    print(f"hey {mylist[r]}")
    r=r+1
#sorting list
mylist.sort()
print(f"sorted list{mylist}")
#reversing the list
mylist.sort(reverse=True)
print(f"reversed list{mylist}")

def myfun(v):
    return abs(v-50)   
num=[23,45,64,67,87,86,43,2]
num.sort(key = myfun)  
print(num)

    

