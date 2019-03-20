x = "Anthony"
y = str.maketrans('nol','xyz')
x = x.translate(y)
print (x)
z = str.maketrans('xyz','nol')
x = x.translate(z)
print (x)
#x[7] = "y"
#x = x[7].replace('o','y')
#print (x)
b = list(x)
b[7] = "y"
print (b)
x = ''.join(b)
print (x)

