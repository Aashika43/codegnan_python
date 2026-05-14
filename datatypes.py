Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int
>>> int(2)
2
>>> int(2.0)
2
>>> int(nagi)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(nagi)
NameError: name 'nagi' is not defined
>>> int("nagi")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("nagi")
ValueError: invalid literal for int() with base 10: 'nagi'
>>> int(4+8j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(4+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(3j+5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(3j+5)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> str(5)
'5'
>>> str(5.6)
'5.6'
>>> str(true)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    str(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> str(True)
'True'
