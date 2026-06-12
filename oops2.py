#diff b/w _ and __
'''class Employee():
    def __init__(self):
        self.name="manu"
        self._mailid="manu@gmail.com"
        self.__salary=100000#private variable
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee__salary)'''

#TASK
'''class Employee:
    def __init__(self, name, mailid, salary):
        self.name = name
        self.mailid = mailid
        self.__salary = salary   # Private Variable
emp1 = Employee("aashika", "aashika@codegnan.com", 100000)
emp2 = Employee("nakshatra", "Nakshatra@gmail.com", 10000000)

print("Employee 1 Details:")
print(emp1.name)
print(emp1.mailid)
print(emp1._Employee__salary)   
print()
print("Employee 2 Details:")
print(emp2.name)
print(emp2.mailid)
print(emp2._Employee__salary)'''

#polymorphism

#operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(8))
print(a.__sub__(1))
print(a.__mul__(5))
print(a.__pow__(2))
#print(a.__div__(2))
print(a.__ge__(6))
print(a.__le__(8))
print(a.__eq__(2))
a=[2,3,4,5,6,7,8];b=[5,6,7,8,9,10,11]
print(a+b)
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(6))
a="code";b="gnan"
print(a+b)
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b))
print("aashu".__add__(" "+"P").title())'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(3)
y=B(4)
#x=3
#y=4
print(x+y)'''

#method overloading
'''class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
a=New()
a.sum()
a.sum(2,4,6)
a.sum(5,6)'''


