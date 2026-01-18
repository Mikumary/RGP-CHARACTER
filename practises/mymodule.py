class employee:
    raise_amount=78


    def __init__(self,first,last,pay):#self are taken as the first commnd in class
        self.first=first
        self.last=last
        self.pay=pay  
        self.email=first + "#" + last + "@gmail.com"   

    def fullname (self):
        return '{} {}'.format(self.first,self.last)
    def raised_amount(self):
        raise_amount=78
        return self.pay + (raise_amount)
    
    @classmethod#decorator
    def set_raise_amount(cls,amount):
         cls.raise_amount=amount

employee.set_raise_amount(47)
        

emp_1=employee("mary",'miku',50000)
emp_2=employee('nick','nyagol',6000)

print(emp_2.fullname())
print(emp_2.raise_amount)
#class methods while using class methods class are used as the main argument

#we want to create a new employee from the employees where they are stringed
emp_str_1="john_maina_9000"
emp_str_2="susan_maina_7800"
emp_str_3="Ruth_mbugua_8000"

#first step is we split them
first,last,pay=emp_str_1.split('_')

new_emp_1=employee(first,last,pay)

print(new_emp_1.fullname())

