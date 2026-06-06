#enumerate() #we can give counter to the collection

'''names=["nakshitra","aashika","mounika","srinidhi","hasini","sophia"]'''
'''for i in range(len (names)):
    print(i,names [i])'''

'''b=list(enumerate(names))
print(b)

b=tuple(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)

b=dict(enumerate(names))
print(b)'''


#annnonymous functions(nameless functions):these functions are nameless functions


#write a function to caluclate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input("value"))
    print(2*x+5)
f()'''


#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

#task
'''a="codegnan"
b=lambda x:x.upper()
print (b(a))'''

'''a="python course"
b=lambda x:x.title()
print(b(a))'''

#first name+last name=full name
'''a=input("fname")
b=input("lname")
c=lambda a,b:(a+" " +b).title()
print(c(a,b))'''

'''a,b=input("enter the names").split(",")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter()
#[],(),{}
'''a=[]
print(type(a))'''

'''b=()
print(type(b))'''

'''c={}
print(type(c))

d=set()
print(type(d))'''

#a=[3,6,8,10,15,20,40,60,100]
'''if a%2==0:
    print(a)'''#error

'''for i in a:
    if i%2==0:
        print(i)

b=list (filter(lambda i:i%2==0,a))
print(b)'''

'''b=[[],set(),{}," ",5,9.0,"python",7+9j,True,False]
c=list(filter(None,b))
print(c)'''

#map()->each object from a collection and forms
#a new collection
'''a=[20,40,50,5,8,9,30,60]
b=[4,6,8,18,25,40,45,60]

c=list(map(max,a,b))
print(c)

d=list(map(min,a,b))
print(d)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=[int(x) for x in input("enter the value").split(",")]
print(a+b)'''

'''a=input ("data1")
b=input("data2")
print(a+b)

a,b=[x for x in input("names").split(",")]
print(a+b)


a=list(map(int,input("enter the names").split(",")))
print(a)'''

'''a=tuple(map(int,input("enter the names").split(",")))
print(a)'''

'''a=set(map(int,input("enter the values").split(",")))
print(a)'''

