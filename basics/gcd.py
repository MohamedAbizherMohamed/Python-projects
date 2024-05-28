import sys
import math

def euclideanalgorithm (p, q):

    while p % q != 0:
        r = p % q
        p = q
        q = r
        
    return q

def main():
    if len(sys.argv) != 3:
        print("Please only input 2 values")

    try:
        p = int(sys.argv[1])
        q = int(sys.argv[2])

    except ValueError:
        print("Please input valid integers")

    gcd = euclideanalgorithm(p, q)
    print(gcd)

if __name__ == "__main__":
    main()