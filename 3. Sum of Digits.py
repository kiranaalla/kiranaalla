i=int(input("Enter a number: "))
result=0
while i>0:
    dig=i%10
    result=result+dig
    i=i//10
    print(result)
