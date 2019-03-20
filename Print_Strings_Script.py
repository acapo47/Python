
>>> import cx_oracle

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import cx_oracle
ImportError: No module named cx_oracle
>>> import cx_Oracle

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import cx_Oracle
ImportError: No module named cx_Oracle
>>> b = "this is a string"
>>> type(b)
<type 'str'>
>>> b = 123
>>> type(b)
<type 'int'>
>>> b = 456.77
>>> type(b)
<type 'float'>
>>> b = "this is a string"
>>> b[0]
't'
>>> b[0] = 'T'

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b[0] = 'T'
TypeError: 'str' object does not support item assignment
>>> b = b.split()
>>> b
['this', 'is', 'a', 'string']
>>> b[0] = 'This'
>>> b
['This', 'is', 'a', 'string']
>>> b = ' '.join(b)
>>> b
'This is a string'
>>> b = 'one fish two fish red fish blue fish'
>>> b = b.split('fish')
>>> b
['one ', ' two ', ' red ', ' blue ', '']
>>> b = b.split('one')

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b = b.split('one')
AttributeError: 'list' object has no attribute 'split'
>>> b = 'fish'.join(b)
>>> b
'one fish two fish red fish blue fish'
>>> 
>>> 
