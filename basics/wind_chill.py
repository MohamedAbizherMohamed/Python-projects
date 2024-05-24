import sys

def windchill(t, v):
    # Calculate the wind chill index using the provided formula
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
    return w

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Please input 2 float values")
        sys.exit(1)

    # Read temperature and wind speed from command line arguments
    t = float(sys.argv[1])
    v = float(sys.argv[2])

    # Calculate wind chill
    wchill = windchill(t, v)

    # Print the result
    print(f"The wind chill index is {wchill}")

if __name__ == "__main__":
    main()
