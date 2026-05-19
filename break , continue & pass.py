#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''

'''for i in range(21):
    if i==14:
        break
    print(i)'''

'''a="python"
if a=="h":
    break
print (a)'''#error

'''a="python"
for i in a:
    print(i)'''

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue'''

'''a=20
while a>5:
    print(a)
    a=a=1'''

'''for i in range (15):
    if i ==9:
        continue
    print(i)'''


'''a="python"
for i in a:
    if i=="h":
        continue
    print(i)'''

#pass
'''a=25
while a>1:
    print (a)
    a=a-1
    if a==15:
        pass'''

'''for i in range (15):
    if i==10:
        pass
    print(i)'''

#ATM APPILICATION
account=100000

    
pwd=2013
card=input("insert the card")
if card=="c":
    print("welcome aashika")
    password=int(input("enter the password"))
    if password==pwd:
        option=int(input("choose the option:1.balance enq 2.withdraw"))
        if option==1:
            print("your acc bal is",account)
        elif option==2:
            money=int(input("enter the amount"))
            print(money)
            balance=account-money
            account=balance
            print("rem acc bal is",balance)
        else:
            print("invalid option")
    else:
        print("incorrect password")
else:
    print("invalid card")

