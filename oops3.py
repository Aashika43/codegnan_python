#method overriding
'''class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("Dog can barks")
c=Animal()
d=Dog()
c.speak()
d.speak()'''

#TASK
'''class Bike():
    def vehicle(self):
        print("GT")
class Car():
    def vehicle(self):
        print("porsche")
c=Bike()
d=Car()
c.vehicle()
d.vehicle()'''

#single inheritance
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        #print("available cash is",cls.cash)
        print("avaliable cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        #print("avaliable cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        #print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#TASK
#MULTIPLE INHERITANCE
#father-Weigth
#mother-Heigth
#kid-Dob
'''class Father:
    def weight(self):
        print("Father's weight: 75 kg")
class Mother:
    def height(self):
        print("Mother's height: 5.2 feet")
class Kid(Father, Mother):
    def dob(self):
        print("Kid's DOB: 23-11-2031")
k = Kid()
k.weight()
k.height()
k.dob()'''

#MULTI-LEVEL
#grandparents-land
#parents-house
#child-vehicle
class Grandparents():
    def land(self):
        print('Grandparents give land')
class Parents(Grandparents):
    def house(self):
        print('Parents give house')
class Child(Parents):
    def vehicle(self):
        print('Child gives bike')
a=Child()
a.land()
a.house()
a.vehicle()

