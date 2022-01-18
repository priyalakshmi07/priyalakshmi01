XYZ=[99,45,89,67]
XYZ.sort()

def find_a_value_in_num(numbers, item):
 for index, value  in enumerate(numbers):
    if value > item:
        return -1
    elif item== value:
        return index
 return -1

found_index = find_a_value_in_num(XYZ,int(input("Enter the value:")))

if found_index != -1:
    print("Found: ", XYZ[found_index])
else:
    print("Not found")
