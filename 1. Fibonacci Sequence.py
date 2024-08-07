n=int(input("enter a number "))
a=0
b=1
sum=0
for m in range (n):
    print(sum,end=" ")
    sum=a+b
    b=a
    a=sum
