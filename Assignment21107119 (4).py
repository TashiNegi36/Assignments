a=int(input("enter side 1"))
b=int(input("enter side 2"))
c=int(input("enter side 3"))
l=[a,b,c]
l.sort()
while(l[0]+l[1]>l[2]):
    print("yes")
    break;
while(l[0]+l[1]<=l[2]):
    print("no")
    break;    
