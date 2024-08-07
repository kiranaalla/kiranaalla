start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
odd_sum = 0
even_sum = 0
print("Odd numbers:")
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num)
        odd_sum += num
print("\nEven numbers:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)
        even_sum += num
print("\nSum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)
print("Total sum of all numbers:", odd_sum + even_sum)
