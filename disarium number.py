num = int(input("Enter a number: "))
num_str = str(num)

sum = 0
for i in range(len(num_str)):
    digit = int(num_str[i])
    position = i + 1
    sum += digit ** position

if sum == num:
    print(num, "is a Disarium number.")
else:
    print(num, "is not a Disarium number.")
