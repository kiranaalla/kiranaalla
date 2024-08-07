a = []
num = int(input("Enter number of elements in the list: "))
for i in range(num):
    b = int(input("Enter element: "))
    a.append(b)
print("Largest element is:", max(a))
