import sys

# Function to calculate the k-th root of c with tolerance e
def root(k, c, e):
    t = c
    
    # Iteratively improve t using Newton's method
    while abs(1 - c / t**k) > e:
        t = t - (t**k - c) / (k * t**(k-1))
        
    return t

# Main function to handle input and call the root function
def main():
    if len(sys.argv) != 4:
        print("Please input 3 numbers")
        sys.exit(1)
    
    try:
        k = int(sys.argv[1])
        c = float(sys.argv[2])
        e = float(sys.argv[3])

    except ValueError:
        print("Please input valid numbers")
        sys.exit(1)
    
    kroot = root(k, c, e)
    print(kroot)

# Entry point of the script
if __name__ == "__main__":
    main()

