Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=10
print(a)
10
b=20
print(b)
20
>>> c=30
>>> print(c)
30
>>> x=40
>>> print(x)
40
>>> z=50
>>> print(z)
50
>>> 10=20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a123=100
>>> print(a123)
100
>>> a0123456=100
>>> print(a0123456)
100
>>> @=30
SyntaxError: invalid syntax
>>> #=9
>>> $=5
SyntaxError: invalid syntax
>>> _=30
>>> print(_)
30
>>> _3=90
>>> print(_3)
90
>>> print=100
>>> print(print)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(print)
TypeError: 'int' object is not callable
>>> name="aashu"
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(name)
TypeError: 'int' object is not callable
>>> n="aashi"
>>> print("aashi")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print("aashi")
TypeError: 'int' object is not callable
>>> print(n)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(n)
TypeError: 'int' object is not callable
