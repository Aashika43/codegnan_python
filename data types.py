Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=5
>>> type(a)
<class 'int'>
>>> b=8.9
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="codegnan
SyntaxError: unterminated string literal (detected at line 1)
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e=4+3j
>>> type(e)
<class 'complex'>
>>> f=2j+6
>>> type(f)
<class 'complex'>
>>> y=True
>>> type(y)
<class 'bool'>
>>> z=flase
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    z=flase
NameError: name 'flase' is not defined
>>> z=False
>>> type(z)
<class 'bool'>
>>> x="true"
>>> type(x)
<class 'str'>
