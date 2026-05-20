#ATM APPILICATION

while True:
    account=100000
     pwd=8821
    card=input("insert the card")
    if card=="c":
        print("welcome aashika")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option
                            1.balance enq
                            2.withdraw'''))
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
