#GENERATORS
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(*a)
print(type(a))'''

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))'''

'''a,b=[int(x) for x in input("enter the value")
     .split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values")
     .split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''

'''a,b=[int(x) for x in input("enter the values")
     .split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
        return a
print(check(a,b))'''

#yield vs return
'''def mygen():
    #return "python"
    #return "java"
    #return "dsa"
    return "python","java","dsa"
print(mygen())'''

'''def mygen():
    yield "vij"
    yield "vzg"
    yield "hyd"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))'''

#max
'''print(max(4,5,6,7,8,9,10,20))'''

#min
'''print(min(4,5,6,7,8,9,10,20))'''

#sum
'''a=3,4,5,6,7,8,9,10
print(sum(a))'''


#built in functions
'''print(dir())
print(dir("__builtins__"))'''

#fromkeys()
'''a="codegnan"
print(a)
print(str(a))
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"aashu")
print(b)

b["o"]="python"
print(b)'''

#eval()
'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

#zip()-> we can combine
a=[10,20,30,40,50,60]
names=["manu","hasi","aashi","aayush","mahathi","nidhi"]
print(a+names)

'''b=zip(a,names)
print(b)'''

b=list(zip(a,names))
print(b)

b=set(zip(a,names))
print(b)
