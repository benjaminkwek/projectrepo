def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# Example usage
if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")