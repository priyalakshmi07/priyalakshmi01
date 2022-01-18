def checkKey(d,key):
    if key in d:
        print("Present, ",end =" ")
        print("value=",d[key])
    else:
     print("Not present")

d={}
user_input=int(input("Enter the dictionary values:"))
for i in range(0,user_input):
    key=input("Enter the key value:")
    value=input("Enter the value:")
    d[key]=value
print("Dict values are",d)
key=input("Enter the key:")
checkKey(d,key)


