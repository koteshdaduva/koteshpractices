n=input()
a=int(n[0])
b=int(n[1])
c=int(n[2])

x=a**3
y=b**3
z=c**3
k=((x+y+z)==int(n))
if k:
    print("True")
else:
    print("False")
