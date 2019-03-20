x = "Anthony"
y = str.maketrans('Ant','xyz')
x = x.translate(y)
print (x)
z = str.maketrans('xyz','Ant')
x = x.translate(z)
print (x)
#x[7] = "y"
#x = x[7].replace('o','y')
#print (x)
b = list(x)
b[7] = "y"
print(b)
x = ''.join(b)
print (x)
#
# Dictionaries
#
d = {'A':[5,7,9],'B':'Harry'}
print (d)
print ('A' in d)
print ('X' in d)
e = dict.fromkeys(['name','age'])
print (e)
e = e.fromkeys(['name','age'],'Got Nothing')
print (e)
print (e.get('a'),'Nothing there')
print (e.get('A', 'Nothing there'))
print (d.items())
print (d.keys())
print (d.values())

x, y, z = 12,14,9
print (x, y, z)
w = x
x = y
y = w
print (x,y, 'Old school')
x, y = y, x
print (x, y)
s = l = 24
print (s,l)
