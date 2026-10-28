def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
        
    return result

try:
    num = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {num} is: {calculate_factorial(num)}")
except ValueError:
    print("Please enter a valid integer.")



