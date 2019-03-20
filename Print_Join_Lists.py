w = "Howzit going?"
print(w[0])
print (w[-1])
print (w[2:5])
print (len(w))

print (w[len(w)- 1])
#w[4] = 'x'

print (w[::])
print (w[:4])
print (w[::2])
print (w[::-1])

print ("spam " * 10)
x = ["spam"] * 6
print (x)
print (x + [1,2,3,4,5])

perm = ['r','w']
print ('r' in perm)
print ('x' in perm)
print (type(w))
w = list(w)
print (type(w))
w = "hOWZIT GOING?"
l = list(w)
print (l)
l = w.split()
print (l)
w = ''.join(l)
print (w)
w = ' '.join(l)
print (w)
l2 = ['one','fish','two','fish','red','fish','blue','fish']
print (l2)
w2 = 'fish'.join(l2)
print (w2)
l = list(w)
l[4] = 'X'
w = ''.join(l)
print (w)


