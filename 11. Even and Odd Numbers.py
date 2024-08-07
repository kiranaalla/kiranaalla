i = input("Enter numbers separated by spaces: ")
n = [int(num) for num in i.split()]
even_numbers = []
odd_numbers = []
for num in n:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
