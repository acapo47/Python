>>> a= 'asdf'
>>> a[3] = 'c'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[3] = 'c'
TypeError: 'str' object does not support item assignment
>>> l = list(a)
>>> l
['a', 's', 'd', 'f']
>>> l[3] = 'c'
>>> l
['a', 's', 'd', 'c']
>>> a = ''.join(l)
>>> a
'asdc'
>>> if True:
	print("It's true")
       print ("Wrong indentation")
       
SyntaxError: unindent does not match any outer indentation level
>>> saleAmount = 74.30
>>> taxable = False
>>> tax = .0825
>>> total = saleAmount + saleAmount * tax * taxable
>>> total
74.3
>>> taxable = True
>>> total = saleAmount + saleAmount * tax * taxable
>>> total
80.42975
>>> a
'asdc'
>>> bool(a)
True
>>> a = ' '
>>> bool(a)
True
>>> a = ''
>>> bool(a)
False
>>> str.isnumeric(str(age))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    str.isnumeric(str(age))
NameError: name 'age' is not defined
>>> 
=============== RESTART: C:/Users/glnn104lab/Desktop/12117.py ===============
Enter a number 1
>>> x = [12, 20, 19, 20, 13]
>>> len (x)
5
>>> range(len(x) + 1)
range(0, 6)
>>> r = range(len(x) + 1)
>>> for z in r:
	print
