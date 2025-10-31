num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    if num > 0:
        print(f"{num} is a natural number.")
    else:
        print(f"{num} is not a natural number (natural numbers start from 1).")
else:
    print("Invalid input. Please enter a valid number.")
