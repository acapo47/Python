age = 220
assert age >= 21
assert age >= 21, 'Don\'t try that fake ID on me'
#assert 21 <= age < 100, 'Get outta here'

s = input("Enter a number ")
while not str.isnumeric(s):
    print("I said a number!")
    s = input("Enter a number ")
    
print(" ")

x = "how"

for z in x:
    print (z)

r = range(12, 20)
for z in r:
    print (z)

d = {'X':12345, 'z':["Anthony","Capo"], 'w':'Howdy',ArithmeticError 3:12}
for x in d:
    print (d[x])

for x, v in d.items():
    print ("Key: ",x," Value: ", v)
print()

while True:
    s = input("Enter a number ")
    if s == 7:
        continue
    
    if str.isnumeric(s):
        print ("Got it")
        break
    print("I said a number!!")
    
