def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Please enter valid numbers")

def multiply_numbers(num1, num2):
    return num1 * num2

def main():
    print("Multiply two numbers")
    num1, num2 = get_numbers()
    result = multiply_numbers(num1, num2)
    print(f"\nThe product of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()