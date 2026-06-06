#pyramid
'''for i in range (1,5):
    for j in range(4-i):
        print(" " ,end="")
    for k in range (i):
        print("*",end=" ")
    print()'''


#right angled reverse
'''for i in range(5,0,-1):
    print ("*"*i)'''


#square pattern
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''

#right angled triangle
'''n=int(input("enter the number of rows: "))
for i in range(1,n+1):
    print("*"*i)'''

#reverse rigth angle
'''n=int(input("enter the number of rows: "))
a=n
for i in range (1,n+1):

            print("*"*a)
            a-=1'''

#functions
'''a=10
b=20
print("the product is",a*b)
print("the sum is",a+b)
print("the diff is",a-b)'''

'''a=1000
b=2000
print("the product is",a*b)
print("the sum is",a+b)
print("the diff is",a-b)'''


'''def caluclate(a,b):
    print("the product is",a*b)
    print("the sum is",a+b)
    print("the diff is",a-b)
caluclate(10,20)
caluclate(100,200)
caluclate(1000,2000)'''

'''a=10
b=20
print("the intdiv",a//b)
print("the mod",a%b)
print("the pow",a**b)'''

'''def add(a,b):
    print(a+b)
add(4,5)'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
add()'''

'''def fullname():
    a=input("first name")
    b=input("last name")
print("a+b")'''


#task

'''a=int(input())
b=int(input())
def operations(a,b):
    c=int(input("1.add,2.sum,3.product"))
    if c==1:
        print("the sum is",a+b)
    if c==2:
        print("the diff is",a-b)
    if c==3:
        print("the product is",a*b)'''


'''while loop:
    
    def cal():
    a=int(input("last name"))
    b=int(input("first name"))
    option=int(input(choose the option
                         1.add
                         2.sub
                         3.mul))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)'''



#multiple def
                         
'''a=int(input('A value: '))
b=int(input('B value: '))
c=int(input('select an option:
                        1.Add
                        2.Sub
                        3.Mul
                        ))
def add(a,b):
    print('The sum is:',a+b)
def sub(a,b):
    print('The diff is:',a-b)
def mul(a,b):
    print('The product is:',a*b)
if c==1:
    add(a,b)
elif c==2:
    sub(a,b)
elif c==3:
    mul(a,b)
else:
    print('invalid option')'''



#print v/s return
'''def add(a,b):
    print(a+b)
add(2,4)'''

'''def add(a,b):
    return(a+b)
print(add(2,5))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,6)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(3,5))'''


#keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="aashika"
    mailid="aashika@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="charitha",mailid="c@gmail.com")
Details(id=30,name="shreya",mailid="s@gmail.com")
Details(40,"aayush","a@gmail.com")
Details("pavan","p@gmail.com",50)
Details(mailid="m@gmail.com",id=60,name="nakshatra")'''


#default arguments

'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",100)'''

'''def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("print is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    #non-def arg follows def avg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''


#task

#cake,price,qty:
'''def Cake(cake,price,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %d" %qty)
Cake("choco",999,500)'''

#spilt bill
'''def spiltbill():
    a=int(input('Enter total bill: '))
    b=int(input('Enter the total number of people: '))
    print("prehead bill is",a//b)
spiltbill()'''

'''def spiltbill():
    a=int(input('Enter total bill: '))
    b=int(input('Enter the total number of people: '))
    c=a//b
    print("prehead bill is {}".format(c))
    print(f"the bill is {c}")
spiltbill()'''

def spiltbill():
    a=int(input('Enter total bill: '))
    b=int(input('Enter the total number of people: '))
    print("prehead bill is {}".format(a//b))
    print(f"the bill is {a//b}")
spiltbill()

