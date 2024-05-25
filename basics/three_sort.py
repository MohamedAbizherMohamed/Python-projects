import sys
import math

def fthree(x, y, z):

    numbers = [x, y, z]

    a = min(numbers)
    b = max(numbers)
    
    if a - x == 0 and b - y == 0 or a - y == 0 and b - x == 0:
        c = z

    if a - x == 0 and b - z == 0 or a - z == 0 and b - x == 0:
        c = y
    
    if a - y == 0 and b - z == 0 or a - z == 0 and b - y == 0:
        c = x

    numbers1 = [a, c, b]
    return numbers1

def main():
    if len(sys.argv) != 4:
        print("please input 3 integers.")
        sys.exit(1)

    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])

    except ValueError:
        print("Please input integers.")
        sys.exit(1)

    three = fthree(x, y, z)
    print(three)

if __name__ == "__main__":
    main()