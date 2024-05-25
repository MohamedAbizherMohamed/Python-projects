import sys
import math

def fsnell(o1, n1, n2):

    o1_rad = math.radians(o1)

    o2 = math.asin(n1 * math.sin(o1_rad) / n2)

    o2_deg = math.degrees(o2)

    return o2_deg

def bob():

    if len(sys.argv) != 4:
        print("Please input 3 numbers")
    
    try:
        o1 = float(sys.argv[1])
        n1 = float(sys.argv[2])
        n2 = float(sys.argv[3])

    except ValueError:
        print(" Please input a number")
    
    snell = fsnell(o1, n1, n2)
    print(snell)

if __name__ == "__main__":
    bob()
