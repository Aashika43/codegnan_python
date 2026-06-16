#TASK

#HIERARCHICAL

#Employee -> company parent
#Trainer -> teaching
#developer -> dovetping
'''class Employee:
    def work(self):
        print("Employees work in the company")

class Trainer(Employee):
    def teaching(self):
        print("Trainer is teaching")

class Developer(Employee):
    def developing(self):
        print("Developer is developing")


t = Trainer()
d = Developer()

t.work()        
t.teaching()    

d.work()        
d.developing()'''

#HYBIRD

#person -> Details
#teacher-> Teach
#student-> Study
#teaching assistant-teacher,student
'''class Person():
    def details(self):
        print('Details of a person')
class Teacher(Person):
    def teach(self):
        print('Teacher teaches')
class Student(Person):
    def study(self):
        print('Student learns')
class TeachingAssistant(Teacher,Student):
    def both(self):
        print('Teaching Assistant assists')
a=Teacher()
b=Student()
c=TeachingAssistant()
a.details()
a.teach()
b.details()
b.study()
c.both()'''

#super()
class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
a=child("aashika",17)
print(a.name)
print(a.age)
