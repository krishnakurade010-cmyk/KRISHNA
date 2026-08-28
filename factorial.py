# Calculate the factorial of a number

number = int(input("Enter a number: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial:", factorial)
