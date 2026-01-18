def my_name():
    print("mary")
my_name()
 
def greet(name):
    print("hello",name)

greet("mary")

def add_two_numbers(a,b):
    return a+b

sumis=add_two_numbers(5,3)
print(sumis)

def input_num():
    num1=float(input("input your first number: "))
    num2=float(input("input your second number: "))
    return num1*num2
result=input_num()
print("the result is: ",result)

def check_grade():
    grade=float(input("whta grade did you get? "))
    if grade>=80 and grade<=100:
        return("Grade: A")
    elif grade>=70 and grade<=79:
        return("Grade: B")
    elif grade>=60 and grade<=69:
        return("Grade: C")
    elif grade>=50 and grade<=59:
        return("Grade: D")
    else:
        return("Grade: F")
results=check_grade()
print("your grade is: ",results)

def count(n):
    if n ==1:
        print("hulee")
    else:
        print(n)
        count(n-1)
        
count(7)

numbers={1,5,6,4,6,8}
doubled=list(map(lambda y:y*2,numbers))
print(doubled)