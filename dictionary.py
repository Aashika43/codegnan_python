Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
#dict()
a={"name":"aashu","year":2026}
print(a)
{'name': 'aashu', 'year': 2026}
type(a)
<class 'dict'>
b={"name","aashu","year",2026}
print(b)
{'name', 'aashu', 'year', 2026}
type(b)
<class 'set'>
a["name"]
'aashu'
a[2026]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[2026]
KeyError: 2026
a.keys()
dict_keys(['name', 'year'])
a.values()
dict_values(['aashu', 2026])
a.items()
dict_items([('name', 'aashu'), ('year', 2026)])
#update
a={"year":2026,"month":"may"}
a.update({"date":12})
a
{'year': 2026, 'month': 'may', 'date': 12}
a.update({"date":12,"time":7})
a
{'year': 2026, 'month': 'may', 'date': 12, 'time': 7}
#set default
a={"mobileno":7995836095,"mailid":"aashu@gmail.com"}
a.setdefault("name","aashu")
'aashu'
a
{'mobileno': 7995836095, 'mailid': 'aashu@gmail.com', 'name': 'aashu'}
a={"colour":"black","food":"coco"}
a.get("colour")
'black'
a.copy()
{'colour': 'black', 'food': 'coco'}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("colour")
'black'
>>> a
{'food': 'coco'}
>>> a.popitem()
('food', 'coco')
>>> a
{}
>>> a={"moblileno":98765,"mail":"a@gmail.com}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> #
...    
>>> a={"name":"aa","city":"vij","name":"aa"}
...    
>>> print(a)
...    
{'name': 'aa', 'city': 'vij'}
>>> a={"name":"aa","city":"vij","name":"an
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a={"name":"aa","city":"vij","name":"na"}
...    
>>> print(a)
...    
{'name': 'na', 'city': 'vij'}
>>> {'name': 'na', 'city': 'vij'
... a={"name":"aa","city":"vij","name1":"aa"}
...  
SyntaxError: '{' was never closed
>>> print(a)
...  
{'name': 'na', 'city': 'vij'}
>>> a={"idno":[10,20,30],"names":["aa","na","va"]}
...  
>>> print(a)
...  
{'idno': [10, 20, 30], 'names': ['aa', 'na', 'va']}
>>> a.keys()
...  
dict_keys(['idno', 'names'])
>>> a.items()
...  
dict_items([('idno', [10, 20, 30]), ('names', ['aa', 'na', 'va'])])
>>> a.values()
...  
dict_values([[10, 20, 30], ['aa', 'na', 'va']])
