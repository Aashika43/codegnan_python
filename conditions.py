#conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=2
b=4
if a<=b:
    print("true")'''
    
'''a=10
b=20
if a>=b:
    print("true")'''


'''a=6
b=12
if a!=b:
      print (" not equal")'''

'''a=2
b=4
if a==b:
    print("true")'''

'''a=4
b=4
if a==b:
    print("true")'''


'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''


'''a=int(input("a value"))
if a<10:
    print("less")'''


'''a="python"
if a=="python":
    print("true")'''


'''a=input("data")
if a=="ds":
    print("match")'''


#if-condition by using logical operators:
#and

'''a=4
b=8
if a<b and b>a:
    print("true")'''

'''a=4
b=8
if a<=b and b>=a:
    print("true")'''

#or
'''a=5
b=10
if a<=b or b>=a:
    print("true")'''

'''a=4
b=8
if a<b or b<a:
    print("true")'''

'''a=4
b=8
if a!=b or b==a:
    print("aashu")'''

#not
'''a=3
b=6
if not a<b:
    print("aayush")'''


'''a=3
b=6
if not a<b and b>a:
    ptint("aayush")'''


'''a=int(input("a value"))
b=int(input("b value"))
if a<b and b>a:
    print("aayush")'''


#if-condition by using identify operators:
#is , is not
'''a=8
if type(a) is int:
    print("it is int")'''

'''a=10
if type(a) is not int:
    print("false")'''

'''a=int(input("value"))
if type(a) is int:
    print("true")'''

'''a=str("enter the value"(" "))
if type(a) is str :
    print("true")'''


#if-condition by using membership operators :
'''a=[1,2,3,4,5,6,7]
if 7 is a :
    print("true")'''


'''a=[1,2,3,4,5,6,7]
if 7 not in a:
    print("true")'''


'''a=int(input("a value"))
if 10 in a:
    print("true")''' #error

'''a=[1,2,3,4,5,6,7]
b=int(input("a value"))
if b in a:
    print("true")'''


#if-else
'''a=2
b=7
if a<b:
    print("true")
else:
    print("false")'''


'''a=2
b=7
if a<b:
    print("true")
else:
    print("false")'''


'''a=2
b=7
if a>b:
    print ("true")
else:
    print("false")'''

#logical using if-else:
'''a=15
b=16
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=9
b=5
if a>b or b<a:
    print("true")
else:
    print("false")'''

#if-else
'''a=2
b=7
if a<b:
    print("True!")
else:
    print("False")'''

'''a=2
b=7
if a>b:
    print("True")
else:
    print("False")'''


'''a=12
b=14
if a>b or b<a:
    print("True")
else:
    print("False")'''

'''a=12
b=14
if a<b or b>a:
    print("True")
else:
    print("False")'''

#Not:

'''a=12
b=17
if not a>b:
    print("True!")
else:
    print("False!")'''

'''a=12
b=17
if not a<b:
    print("True!")
else:
    print("False!")'''

#Membership operators:
'''a=[1,2,3,4]
if 3 in a:
    print("Present!")'''

'''b=[4,5,6,7]
if 1 not in b:
    print("Not present!")'''

#identify operators:
a=12
if type(a)is int:
    print("Its int!")

a=13
if type(a) is not int:
    print("Its not!")

a=12.0
if type(a)is float:
    print("Its float")
