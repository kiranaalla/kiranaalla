n=int(input("Enter a number:"))
for row in range(1,n+1):
    for space in range(1,row):
        print(" ",end="")
    for stars in range(1,n-row+1):
        print("*",end="")
    print()
