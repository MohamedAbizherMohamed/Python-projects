import sys
import math

def root(k, c, e):
    t = c
    
    while abs(1 - c / t**k) > e:
        t = t - (t**k - c) / (k * t**k-1 )
        
    return t

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

if __name__ == "__main__":
    main()
