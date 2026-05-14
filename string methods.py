Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len
9
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
a.count ("twinkle")
2
a.count("k")
2
a.count(" ")
3
#escape sequences
#\n-> new line
#\t-> tab space
a="name\nmobileno\tmailid"
print(a)
name
mobileno	mailid
b="name:aashu\nmobileno:7995836095\tmailid:aashi@gmail.com"
print(b)
name:aashu
mobileno:7995836095	mailid:aashi@gmail.com
#replace()
a="wait until you succed"
a.replace("wait","work")
'work until you succed'
#find a string
a="code"
a[0]
'c'
a.find("d")
2
#upper()
a="python"
a.upper()
'PYTHON'
#lower()
b="hello"
b.lower()
'hello'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
d[3].upper()
'H'
a="hello"
a.isupper()
False
a.islower()
True
b="hello world"
b.isalpha()
False
c="hellowworld"
c.isalpha()
True
d=890
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="123456"
e.isdigit()
True
x="aashika21"
x.isalnum()
True
#strip()
#lstrip()
#rstrip()
a="       aashu    "
a.strip()
'aashu'
a.lstrip()
'aashu    '
a.rstrip()
'       aashu'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']
#join()
a="python","c","c++"
"".join(a)
'pythoncc++'
>>> " ".join(a)
'python c c++'
>>> #concatenation
>>> a="python"
>>> b="course"
>>> print(a+b)
pythoncourse
>>> print(a+ " " + b)
python course
>>> fname=aashika
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    fname=aashika
NameError: name 'aashika' is not defined
>>> fname="aashika"
>>> lname="p"
>>> print (fname+ " " + lname)
aashika p
>>> print((fname+ " "+lname)titile())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> #formstion
>>> #formation
>>> a=3
>>> b=7
>>> print(a+b)
10
>>> print("the sum is",a+b)
the sum is 10
>>> print("the sum is,a+b")
the sum is,a+b
>>> city="vja"
>>> print("city is,vja")
city is,vja
>>> #format method
>>> a="prav"
>>> b="karm"
>>> print("hello {}{}".format(a,b))
hello pravkarm
>>> print("hello {] {}".format(a,b))
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print("hello {] {}".format(a,b))
ValueError: unexpected '{' in field name
>>> print("hello {} {}" .format(a,b))
hello prav karm
>>> #fstring
>>> a="aashi"
>>> b="aayush"
>>> print(f"hello {a} {b}")
hello aashi aayush
>>> print(f"hello {a} hello {b}")
hello aashi hello aayush
