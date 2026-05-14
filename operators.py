Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=4
b=2
print(a+b)
6
print(a-b)
2
print(a*b)
8
print(a//b)
2
print(a/b)
2.0
print(a^b)
6
print(a%b)
0
print(a**b)
16
#assignments
a=2
b=5
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
7
a-=3
a
4
a*=6
a
24
a//=4
a
6
a/=5
a
1.2
a**=9
a
5.1597803519999985
a%=8
a
5.1597803519999985
a%=3
a
2.1597803519999985
print(b+=a)
SyntaxError: invalid syntax
b+=a
b
7.1597803519999985
b-=4
b
3.1597803519999985
b%=2
b
1.1597803519999985
b/=2
b
0.5798901759999993
a=5
b=10
a<b
True
a>b
False
b>a
True
b<a
False
a!=b
True
a==b
False
b==a
False
b<=a
False
a<=b
True
a=6
b=6
print(a<=b)
True
4<9
True
#logical operators
a=8
b=12
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or a>b
True
a>=b or a<=b
True
a!=b or a==b
True
#identify
a=10
if type (a) is int:
    print("it is int)
          
SyntaxError: unterminated string literal (detected at line 2)
if type (a) is int
          
SyntaxError: expected ':'
if type (a) is int :
          print ("it is int")

          
it is int
if type (a) is not int
          
SyntaxError: expected ':'
if type (a) is not int :
          print (true)

          
#membership
          
a=1,2,3,4,5,6,7,8,9,10
          
if 10 in a :
          print(a)

          
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
if 10 in a :
          print(10)

          
10
if 20 in a:
          print(20)

          
if 20 not in a :
          print(20)

          
20

if 20 not in a:
          print("not there")

          
not there
#bitwise
          
#&
          
a=3
          
b=5
          
a=4
          
b=6
          
bin(4)
          
'0b100'
bin(6)
          
'0b110'
a&b
          
4
bin(7)
          
'0b111'
bin(9)
          
'0b1001'
a=3
          
b=2
          
a|b
          
3
#~ (negotiation)
...           
>>> a=4
...           
>>> -(x+1)
...           
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    -(x+1)
NameError: name 'x' is not defined
>>> -(a+1)
...           
-5
>>> #^ (eor)
...           
>>> a=5
...           
>>> b=9
...           
>>> a^b
...           
12
>>> a=10
...           
>>> b=2
...           
>>> a^b
...           
8
>>> #<< (left shift)
...           
>>> a=4
...           
>>> a<<2
...           
16
>>> a=5
...           
>>> a<<3
...           
40
>>> #>>(right shift)
...           
>>> a=6
...           
>>> a>>2
...           
1
>>> a=3
...           
>>> a>>4
...           
0
