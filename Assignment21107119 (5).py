a=int(input("enter a"))
b=int(input("enter b"))
x=a^b
count = 0
while x:
	count += 1
	x &= (x-1)


print(count)
