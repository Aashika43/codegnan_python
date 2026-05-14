Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"python",5+9j,True,False]
print(a)
[2, 5.6, 'python', (5+9j), True, False]
#append()
a=["python","java","c"]
a.append("ml")
a
['python', 'java', 'c', 'ml']
a.append("dsa","ai")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.append("dsa","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["dsa","ai"])
a
['python', 'java', 'c', 'ml', ['dsa', 'ai']]
#extend()
a=["ml","ai","c"]
a.extend(["python","java"])
a
['ml', 'ai', 'c', 'python', 'java']
#insert()
a=["apple","banana","grapes"]
a.insert(1,"mango")
a
['apple', 'mango', 'banana', 'grapes']
#index()
a=["black","pink","red","white]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["black","red","pink"]
   
a
   
['black', 'red', 'pink']
#clear()
   
a.clear[]
   
SyntaxError: invalid syntax
a.clear()
   
a
   
[]
a=["c","ml","java","ai"]
   
a.sort()
   
a
   
['ai', 'c', 'java', 'ml']
b=[8,6,4,3,2,9,1]
   
b.sort()
   
b
   
[1, 2, 3, 4, 6, 8, 9]
#reverse
   
a=["python","java","c"]
   
a.reverse()
   
a
   
['c', 'java', 'python']
b=[1,2,3,4,5]
   
b.reverse()
   
b
   
[5, 4, 3, 2, 1]
#pop
   
a=["hi","hello","hey"]
   
a.pop()
   
'hey'
a
   
['hi', 'hello']
a.pop("hello")
   
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.pop("hello")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
   
'hello'
a
   
['hi']
a="python"
   
len(a)
   
6
b=["python"]
   
len(b)
   
1
#count()
   
b=["c","java","c++","c"]
   
b.count("c")
   
2
b.count("java")
   
1
#tuple()
   
a=(5,6.7,"aashu",4+9j,True,False)
   
print(a)
   
(5, 6.7, 'aashu', (4+9j), True, False)
type(a)
   
<class 'tuple'>
len(a)
   
6
a.count(true)
   
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.count(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
a.count(True)
   
1
a.index(4+9j)
   
3
#sets
   
#sets{}
   
a={3,5.7,"python",8+9j,True,False}
   
print(a)
   
{False, True, 'python', 3, (8+9j), 5.7}
a={1,2,3,4,5,6}
   
a.add(10)
   
a
   
{1, 2, 3, 4, 5, 6, 10}
#issubset()
   
a={1,2,3,4,5,6}
   
b={3,4,5}
   
b.issubset(a)
   
True
a.issubset(b)
   
False
a={4,5,6,7,8,9}
   
b={5,6,7,8}
   
a.issuperset(b)
   
True
#union()
   
a={3,4,5,6,7}
   
b={1,2,3,4,5,6,7,8,9}
   
a.union(b)
   
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a={2,3,4,5,6,7,8,9}
   
b={5,1,8,0,6}
   
a.intersection(b)
   
{8, 5, 6}
#update()
   
a={10,11,12,13,14,15,16}
   
b={13,14,18,16}
   
a
   
{16, 10, 11, 12, 13, 14, 15}
a.update(b)
   
a
   
{10, 11, 12, 13, 14, 15, 16, 18}
a
   
{10, 11, 12, 13, 14, 15, 16, 18}
b
   
{16, 18, 13, 14}
a={2,3,4,5,6,7,8,}
   
b={7,8,9,10}
   
a.difference(b)
   
{2, 3, 4, 5, 6}
b.difference(a)
   
{9, 10}
a={1,2,3,4,5}
   
b={4,5,6,7,8}
   
a.symmetric_difference(b)
   
{1, 2, 3, 6, 7, 8}
b.symmetric_difference(a)
   
{1, 2, 3, 6, 7, 8}
a={6,7,8,9,10}
   
b={1,3,5,6,7,8}
   
a.difference_update(b)
   
a
   
{9, 10}
a
   
{9, 10}
b.update
   
<built-in method update of set object at 0x00000221A1469EE0>
b.update(a)
   
b
   
{1, 3, 5, 6, 7, 8, 9, 10}
b
   
{1, 3, 5, 6, 7, 8, 9, 10}
a={3,4,5,6,7,8}
   
b={6,7,8,9,10,11}
   
a.symmeteric_difference_update(b)
   
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.symmeteric_difference_update(b)
AttributeError: 'set' object has no attribute 'symmeteric_difference_update'. Did you mean: 'symmetric_difference_update'?
b.symmetric_difference(a)
   
{3, 4, 5, 9, 10, 11}
#intersection_update
   
a={10,20,30,40,50,60}
   
b={40,50,60,70,80}
   
a.intersection_update(b)
   
a
   
{40, 50, 60}
b.intersection_update(a)
   
b
   
{40, 50, 60}
a={6,7,8,9,10,11,12,13,1,4}
   
a.pop()
   
1
a.pop(11)
   
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.pop(11)
TypeError: set.pop() takes no arguments (1 given)
a.remove(10)
   
a
   
{4, 6, 7, 8, 9, 11, 12, 13}
>>> #discard
...    
>>> a={5,6,7,8,9}
...    
>>> a.discard(9)
...    
>>> a
...    
{5, 6, 7, 8}
>>> a.index(2)
...    
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(8)
...    
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    a.count(8)
AttributeError: 'set' object has no attribute 'count'
>>> a={4,5,6,7,8,9}
...    
>>> b={1,2,3,4,5,6}
...    
>>> a.isdisjoint(b)
...    
False
>>> a={1,2,3}
...    
>>> b={4,5,6}
...    
>>> a.isdisjoint(b)
...    
True
>>> #clear()
...    
>>> a={5,6,7,8,9}
...    
>>> a.clear()
...    
>>> a
...    
set()
>>> b=set()
...    
>>> b.add(10)
...    
>>> b
...    
{10}
