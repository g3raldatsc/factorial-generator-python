import time

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        time.sleep(0.2)
        print(f"Calculating: {i}! = {result}")
    return result

def main():
    print("Factorial Generator")
    print("===================")
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print("\nProcessing...\n")
    time.sleep(1)
    result = factorial(num)
    print(f"\nThe factorial of {num} is: {result}")

if __name__ == "__main__":
    main()