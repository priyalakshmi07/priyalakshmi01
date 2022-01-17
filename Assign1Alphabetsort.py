string=[]
string = [str(x) for x in input("Enter values\n").split(',')]
sorted_value=string
separator=","
print(separator.join(sorted(sorted_value)))
