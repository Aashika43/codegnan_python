#oops
#syntax
'''class classname():
    name="aashu"
    age=17
    city="vij"
    def fname(method_name):
        print("statements.......")
obj=classname()
print(dir(a))
obj.fname()'''

#class declaration
'''class Details():
    name="aashu"
    age=17
    place="vij"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))'''

#object instantiation

'''class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("aashu",17,"vij")
a.display()
a.Data("aayush",13,"vij")
a.display()
b=Details()
b.Data("baba",26,"vij")
b.display()'''

#object initialization
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("cherry",17,"vij")
print(dir(a))
a.display()'''

#TASK
'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def display(self):
        print(self.name,self.age,self.place)

name=input("Enter name: ")
age=int(input("Enter age: "))
place=input("Enter place: ")

a=Details(name,age,place)

print(dir(a))
a.display()'''


    
