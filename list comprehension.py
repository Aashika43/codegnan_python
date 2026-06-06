#list comperhension
'''a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]
b=str(a)
print(b.upper())'''

'''a=["vij","hyd","vzg"]
#["Vij","Hyd","Vzg"]
b=[i.title() for i in a]
print(b)'''

'''a=[2,4,6,8,12,13]
#[4,16,36,49,64,144,169]
b=[i**2 for i in a]
b=[pow(i,20 for i in a]
b=[i*ifor i in a]
print(b)'''

#if-usage in list comprehension
'''a=[i for i in range (16)]
print(a)'''

'''a=[i for i in range (16) if i%2==0]
print(a)'''

'''a=[i for i in range (16) if i%2!=0]
print(a)'''

'''fruits=["apple","grapes","mango","kiwi","dragon","berry"]
a=[i for i in fruits if "a" in i]
print(a)'''


'''fruits=["apple","grapes","mango","kiwi","dragon","berry"]
a=[i for i in fruits if "a" not in i]
print(a)'''


'''a=[i**2 if i%2==0 else i*5 for i in range (21)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
c=[5+1,2+4,3+3,4+2,5+1]
print(c)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
c=[a[i]+b[i] for i in range(5)]
print(c)
