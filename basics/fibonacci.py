import sys

# Function to calculate the n-th Fibonacci number
def fib(n):
    # Initialize the first two Fibonacci numbers and the loop counter
    a, b = 1, 1
    i = 3

    # Loop to calculate Fibonacci numbers up to the n-th number
    while i <= n:
        # Calculate the next Fibonacci number
        c = a + b
        # Update a and b to the next pair of Fibonacci numbers
        a = b
        b = c
        # Increment the loop counter
        i += 1

    # Return the n-th Fibonacci number
    return b

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        print("Please input one number only")
        sys.exit(1)
    
    try:
        # Convert the command-line argument to an integer
        n = int(sys.argv[1])

    except ValueError:
        # Print an error message if the argument is not a valid integer
        print("Please input a valid integer")
        sys.exit(1)

    # Check if the integer is negative
    if n < 0:
        print("Integer cannot be negative")
        sys.exit(1)

    # Calculate the n-th Fibonacci number
    ans = fib(n)
    # Print the result
    print(ans)

# Entry point of the script
if __name__ == "__main__":
    main()



