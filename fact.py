
#0,1,1,2,3..


N=int(input("Enter the number of factorial numbers to be displayed"))
a=[]
a=0
b=1

for i in range(1,N):
    k=a+b
    a=b
    b=k
print (k)


