score=input("Enter the score:")
try:
    xh= float(score)
except:
   print("Bad score")
   quit()
if xh>=0.9:
 print("A Grade")
elif xh>=0.8:
 print("B Grade")
elif xh>=0.7:
 print("C Grade")
elif xh>=0.6:
 print("D Grade")
elif xh<0.8:
 print("F Grade")
else:
 print("Bad score")
