#swaping of two numbers
a=10
b=20


1.
'''a,b=b,a
print(a,b)'''



2.
'''c=a
a=b
b=c
print(a,b)'''



3.
'''a=a+b
b=a-b
a=a-b
print(a,b)'''



4.
'''a=10
b=20
temp=a
a=b
b=temp
print("a value is",a)
print("b value is",b)'''



'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))'''



#swapping string
'''a="aashu"
b="vaish"
temp=a
a=b
b=temp
print("after swapping a=%s,b=%s" %(a,b))'''



#swapping float
'''a=2.5
b=3.9
a,b=b,a
print("after swapping a=%f,b=%f" %(a,b))'''


'''a=float(input("a value"))
b=float(input("b value"))
a,b=b,a
print("after swapping a=%.2f,b=%.2f" %(a,b))'''


'''a=[9,1,5,2,8,4,6,3,7,0]
print("7,6,4,3,0,9,8,5,2,1")'''


'''a=[9,1,5,2,8,4,6,3,7,0]
b=[7,6,4,3,0]
c=[9,8,5,2,1]
print(b+c)'''


'''a=[9,1,5,2,8,4,6,3,7,0]
a1=a[0:5]
a1
a2=a[5:10]
a2
a1.sort()
a1
a2.sort()
a2
a1.reverse()
a1
a2.reverse()
a2
print(a2+a1)'''


a=["codegnan","python","course"]
#upper()
'''a1=a[0]
b1=a1.upper()
a2=a[1]
b2=a2.upper()
a3=a[2]
b3=a3.upper()
c=[]
c=[b1,b2,b3]
print(c)'''


'''a=["codegnan","python","course"]
b=str(a)
c=b.upper()
print(c)'''


#append
'''a=[0,1,2,3,4,5,6]
a.append(10)
print(a)'''


'''a=[4,6,7,8,9,10]
a.insert(1,5)
print(a)'''


'''a=(5,6,7,8,9,10,11,12)
b=list(a)
b
b.remove(11)
b
c=tuple(b)
c
print(c)'''


a={"year":2026,"month":5}
#{"year":2026,"month":5,"date:13}
a.update({"date":13})
a







