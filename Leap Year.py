y=int(input())
x=((y%400)==0)
z=(((y%4)==0)and ( (y%100)!=0))
if x or z :
    print(True)
else:
    print(not(True))
