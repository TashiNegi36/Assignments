print("Python is a case sensitive language")
string="Python is a case sensitive language"
lengthofstring=len(string)
print(lengthofstring)
reverse_string=string[::-1]
print(reverse_string)
x=slice(10,26)
sliced_string=string[x]
print(sliced_string)
index_a=string.index("a")
print(index_a)
newstring=""
for i in string:
    if i!=" ":
        newstring=newstring+i
print(newstring)        
        
        
