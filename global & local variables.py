#global &local variables:
#first case of global variable
'''a=2
def check1():
    print("a value is ",a)
check1()
print("a value is",a)'''


#second case of global variable
'''a=3
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case of both global and local varibles
'''a=4
b=8
def check3():
    a=6
    print("a value is",a)
    a=10
    print("a value is",a+5)
    b=12#local variable
    b=b+a
    print("b value is",b)
    check3()
print("a value is",a)
print("b value is",b)'''

#usage of global keyword
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("update value is",a)
    #global b
    b=20
    b=b+a
    print("b value is",b)
final()
print("value of a is",a)
print("value of b is",b)'''


#MARKS ANALYISIS REPORT

'''a=int(input('Total no of students: '))
c=[]
d=0
for i in range(1,a+1):
    marks=int(input(f'Enter student {i} marks: '))
    c.append(marks)
    d+=marks
print('Total marks: ',d)
print('Highest marks: ',max(c))
print('Lowest marks: ',min(c))
print('Avg marks: ',d/a)'''

#ASCII
'''print(chr(98))
print(ord("a"))'''

#task
'''for i in range(97,123):
    print(chr (i),end=" ")#a-z
for i in range(65,91):
    print(chr (i),end=" ")#A-Z'''

#TASK2
a=input("enter your name")
for i in a:
    print(i,"-",ord (i))
          






