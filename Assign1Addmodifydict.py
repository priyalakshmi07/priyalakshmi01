dict={}
while True:
    user_input=input("Do you want to Add/Modify Dictionary or Exit:")
    if user_input== 'Add':
        key=input("Enter the key to add:")
        value=input("Enter the value to add:")
        dict[key]=value
        print(dict)
        continue
    elif user_input=='Modify':
        key=input("Enter the key to modify:")
        value=input("Enter the value to Modify:")
        dict.update({key:value})
        print(dict)
        continue
    else: user_input=='Exit'
    break
