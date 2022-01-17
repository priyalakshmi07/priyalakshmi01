string=input("Enter string:")
count1=0
count2=0
for i in string:
    if(i.islower()):
        count1=count1+1
    elif(i.isupper()):
        count2=count2+1
print("The number of lower case character is:",count1)
print("The number of upper case character is:",count2)
