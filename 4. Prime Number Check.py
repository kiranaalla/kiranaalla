n = int(input("Enter a number: "))
if n == 2:
    print("It's a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number")
    else:
        print("Not a prime number")
