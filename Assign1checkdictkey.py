dict={}
dict=input("Enter the dict value:")
key=input("Enter the key value:")
#def checkKey(dict,key):
if key in dict:
    print("Present, ",end =" ")
    print([key for key in dict.keys()][k])
    print("value:",dict[k])
else:
     print("Not present")

#checkKey(dict,key)
