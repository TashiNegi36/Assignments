word=input("enter word")
for i in range(len(word)-1):
    
    if i+3<len(word)-1 and word[i]+word[i+1]+word[i+2]+word[i+3]=="name":
        print("yes")
    else:
        print("no")