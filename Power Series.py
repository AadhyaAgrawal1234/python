x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

print("\nPower series:")

for i in range(n + 1):
    term = x ** i
    if i < n:
        print(term, end=" , ")
    else:
        print(term)

