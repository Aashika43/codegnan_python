#* arguments-> * is used to unpack the elements
'''a=[4,5,6,7,8,9]
print(a)
print(*a)'''

'''a=(4,5,6,7,8,9)
print(a)
print(*a)'''

'''a={4,5,6,7,8,9}
print(a)
print(*a)'''

'''a={"name"%"pooja","year":2026}
print(a)
print(*a)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#error

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error

#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(3,4,5,6,7,8,9)
b=[3,4,5,6,7]
check(*b)
c={8,9,10}
check(*c)
d={"year":2026,"month":5}
check(*d)'''


'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5)
check1(2,4,5.3,2.3)
check1(1,3,4,5,2.3,4.5,"aashu")'''


#task

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
        print(d)
check1()
check1(2,3,4,5)
check1(2,4,5.3,2.3)
check1(1,3,4,5,2.3,4.5,"aashu",4+3j,True,False)'''

'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)

check2()
details={"names":["aashi","aayush","manu","hasi"],
         "status":["p","a","a","p"]}
check2 (**details)'''

#both * and ** usage
'''def final (*a,**b):
    d=2#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type (i) in(int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,4,4.5,3.3,"soppi",2+7j,True,False)
final(*data)
details={"names":["sudheer","phani","rani"],
         "status":["p","a","p"]}

final(**details)
final(*data,**details)'''

#task2
'''marks=[90,80,70,60,95]
totalstudents=len(marks)
highest=max(marks)
lowest=min(marks)
totalmarks=sum(marks)
average=totalmarks/totalstudents
print("Total Students:",totalstudents)
print("Highest Marks:",highest)
print("Lowest Marks:",lowest)
print("Total Marks:",totalmarks)
print("Average:",average)'''

a=int(input('Total no of students: '))
c=[]
d=0
for i in range(1,a+1):
    marks=int(input(f'Enter student {i} marks: '))
    c.append(marks)
    d+=marks
print('Total marks: ',d)
print('Highest marks: ',max(c))
print('Lowest marks: ',min(c))
print('Avg marks: ',d/a)

