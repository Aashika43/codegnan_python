Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a=vijayawada
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=vijayawada
NameError: name 'vijayawada' is not defined
a="vijayawada"
a[2]
'j'
a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'
a="i am in class "
a[5]+a[6]
'in'
a="vijayawada is a royal city"
a[14]+a[15]+a[16]+a[17]+a[18]
'a roy'
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a="vizag is a city of destiny"
a[0]+a[1]+a[2]+a[3]+a[4]
'vizag'
a[11]+a[12]+a[13]+a[14]
'city'
a[19]+a[20]+a[21]+a[22]+a[23]+a[24]+a[25]
'destiny'
a="codegnan it solutions"
a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solutions'
a[-20]+a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]+a[-13]
'odegnan '
b="i love python"
b[-11]+b[-10]+b[-9]+b[-8]
'love'
b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'python'
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[ :4]
'code'
a="work until you succeed"
a[15:21]
'succee'
a[15:22]
'succeed'
a[11:14]
'you'
a[0:4]
'work'
b="simple is better then complex"
a[5:10]
'until'
b[22:29]
'complex'
b[10:16]
'better'
b[0:6]
'simple'
a="kill them with your success
SyntaxError: unterminated string literal (detected at line 1)
a="kill them with your success"
a[-17:-13]
'with'
a[-12:-9]
'you'
a[-27:-23]
'kill'
a[-7:0]
''
a[-7:]
'success'
a="all is well"
a[-7:-5]
'is'
a[-11:-8]
'all'
a[-4:]
'well'
#striding
a="cloud computing"
a[::3]
'cucpi'
a[::5]
'c u'
>>> a[::7]
'cog'
>>> a[::4]
'cdmi'
>>> a[1:6
... a[1:6]
...   
SyntaxError: '[' was never closed
>>> a[1:6]
...   
'loud '
>>> a[5:]
...   
' computing'
>>> a[:9]
...   
'cloud com'
>>> a[7:12]
...   
'omput'
>>> a="machine learning]
...   
SyntaxError: unterminated string literal (detected at line 1)
>>> a="machine learning"
...   
>>> a[1:7:2]
...   
'ahn'
>>> a[2:14:3]
...   
'cnlr'
>>> a[3:15:5]
...   
'hli'
>>> a[5:12:2]
...   
'n er'
>>> a="python course"
...   
>>> a[-1:-8:-3]
...   
'eu '
>>> a[-2:-12:-4]
...   
'sch'
>>> a[-3:-13:-5]
...   
'rn'
>>> a[-5:-11:-2]
...   
'o o'
