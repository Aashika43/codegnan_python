Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#using formation method
#using f-string
a=4
b=5
print(f"multipication of {a} and {b} is {a*b}")
multipication of 4 and 5 is 20
a=9
b=10
print(f"multipication of {a} and {b} is {a*b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
a=6
      
b=3
      
c=a*b
      
print("the product is",c)
      
the product is 18
print("the product is",c)
      
the product is 18
a=10
      
b=20
      
c=(a|b)
      
>>> 
>>> #swaping
...       
>>> a=2
...       
>>> b=3
...       
>>> "replace(a) as (b)"
...       
'replace(a) as (b)'
>>> print "replace (a) as (b)"
...       
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> 'print and replace the values of (a) as (b)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> a=10
...       
>>> b=20
...       
>>> a=a-b
...       
>>> b=b-a
...       
>>> print (a,b)
...       
-10 30
>>> a=10
...       
>>> b=20
...       
>>> a,b=b,a
...       
>>> print(a)
...       
20
>>> print(b)
...       
10
>>> a=10
...       
>>> b=20
...       
>>> temp=a
...       
>>> a=b
...       
>>> b=temp
...       
>>> print(a,b)
...       
20 10
