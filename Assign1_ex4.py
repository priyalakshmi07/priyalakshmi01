num=[]
num= [int(x) for x in input("Enter values\n").split(',')]
import math
result_list = []
for D in num:
    Q= round(math.sqrt(2*50*D/30))
    result_list.append(Q)
separator=","
print(separator.join(map(str,result_list)))
