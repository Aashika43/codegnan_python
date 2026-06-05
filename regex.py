#regex(regular expressions)
'''a="codegnan is in vij"
print(a)'''

'''a="codegnan\nis\tin\nvija"
print(a)'''

#rstring
'''a=r"codegnan\nis\tin\nvija"
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence chareacters
'''\\w->it matches alphanumeric
\\W->it matches non-alphanumeric
\\d->it matches any digit
\\D->it matches non-digits
\\s->it represents white spaces
\\S->it represents non-white spaces'''

#compile()
import re
a="mat map cat money cash maths cap cup code monkey dog donkey"
'''b=re.compile(r"m\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)'''

'''d=re.search(r"m\w+",a)
print(d)'''

#findall
'''d=re.findall(r"m\w+",a)
print(*d)'''

#split()

'''e=re.split(r"m",a)
print(e)

f=re.split(r"\s",a)
print(f)'''

#sub()
'''x.re.sub(r"maths","science",a)
print(x)'''

#\d
'''v='1 hot 4 numb 3 taps wine'
u=re.findall(r'\d',v)
print(*u)'''

#error handling
#syntax error
'''for i in range(10):
    print(i)'''
    
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''

#logical error
'''a=10
b=20
if a<b:
    print("true")'''

'''a=10
b=20
if a>b:
    print("true")'''

#exception handiling
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("expection is raised")
    else:
        print("no exceptional")
    finally:
        print("program ends...")
