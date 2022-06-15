s=input("enter string:")
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")

x=int(input("enter number"))
range1=int(input("enter lower limit"))

range2=int(input("enter upper limit"))
for i in range(range1,range2+1,1):
    if (i%x==0):
        print(i," is divisible by ",x)

x1=int(input("enter side"))
x2=int(input("enter side"))
x3=int(input("enter side"))

s=(x1+x2+x3)/2
l=[x1,x2,x3]
l.sort()
print(l)
if(l[-1]<=s):
    a=s*(s-x1)*(s-x2)*(s-x3)
    a=a**(0.5)
    print(a)
else:
    print("not possible")

x=int(input("enter number"))
for i in range(x):
    for j in range(i):
        print("*",end=" ")
    print("\n")
for i in range(x):
    for j in range(x-i):
        print("*",end=" ")
    print("\n")

s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=int(input("enter number"))
z=0
for i in range(x+1):
    for j in range(i):
        print(s[z],end="")
        z=z+1
    print("\n")

x = int(input("enter lower limit"))
y = int(input("enter upper limit"))
for i in range(x, y + 1, 1):
    p = 0
    for j in range(2, i):
        if (i % j == 0):
            p = p + 1
    if (p == 0):
        print(i, 'is a prime number')

for i in range(501):
    if (i % 77 == 0):
        print(i)

l=[]
for i in range(10):
    x=int(input("enter number"))
    l.append(x)
even=[]
for i in l:
    if(i%2==0):
        even.append(i)
odd=[]
for i in l:
    if(i%2!=0):
        odd.append(i)
neg=[]
for i in l:
    if(i<0):
        neg.append(i)
pos=[]
for i in l:
    if(i>0):
        pos.append(i)
print("even:",even)
print("positive:",pos)
print("negetive:",neg)
print("odd:",odd)
k=[]
for i in l:
    if i not in k:
        k.append(i)
z=0
for i in k:
    for j in l:
        if(i==j):
            z=z+1
    print(i," occurs ",z,"times")



x=int(input("enter number of elements"))
l=[]
k=[]
for i in range(x):
    z=input("enter element")
    l.append(z)
for i in l:
    if i not in k:
        k.append(i)


for i in k:
    z=0
    for j in l:
        if(i==j):
            z=z+1
    print(i," occurs ",z,"times")