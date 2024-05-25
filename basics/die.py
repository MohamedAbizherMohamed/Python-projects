import sys
import random

def fdie(n):
    
    # Generate two random integers between 1 and n
    x = random.randint(1, n)
    y = random.randint(1, n)

    # Sum the two random integers
    sum = x + y

    return sum

def main():

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Please input 1 integer.")
        sys.exit(1)

    try:
        # Convert the first argument to an integer
        n = int(sys.argv[1])
    except ValueError:

        # Handle invalid integer input
        print("Please input an integer.")
        sys.exit(1)

    # Check if the integer is positive
    if n <= 0:
        print("Please provide a positive integer.")
        sys.exit(1)
    
    # Calculate and print the sum of two dice rolls
    die = fdie(n)
    print(die)

if __name__ == "__main__":
    main()


    