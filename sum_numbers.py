def get_ten_numbers():
    numbers = []
    for i in range(10):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number")
    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def main():
    print("Please enter 10 numbers:")
    numbers = get_ten_numbers()
    total = calculate_sum(numbers)
    print(f"\nThe sum of all numbers is: {total}")

if __name__ == "__main__":
    main()