a=int(input("enter first angle"))
b=int(input("enter second angle"))
c=int(input("enter third angle"))
if(a<90 & b<90 & c<90):
    print("it is acute angled triangle")
elif(a==90 & b==90 & c==90):
    print("it is a right angled triangle")
elif(a>90 & b>90 & c>90):
    print("it is a obtuse angled triangle")
else:
    print("no triangle formed")
