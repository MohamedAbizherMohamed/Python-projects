import sys

def fbmi(w, h):

    # Set bmi to weight divided by square of height .
    b = w / (h * h)

    weightrange = ["underweight", "normal", "overweight"]

    if b < 18.5:
        return b, weightrange[0]
    if 18.5 < b < 24.9:
        return b, weightrange[1]
    if b > 24.9:
        return b, weightrange[2]


def main():

    if len(sys.argv) != 3:
        print("Please input 2 float values only")
        sys.exit(1)

    # Accept weight ( float ) and height ( float ) as command - line arguments .
    try:
        w = float(sys.argv[1])
        h = float(sys.argv[2])

    except ValueError:
        print("Please input numbers only")
        sys.exit(1)

    if w < 0 or h < 0:
        print("Weight/height cannot be negative.")
        sys.exit(1)

    # Instansiate object and Print BMI.
    bmi = fbmi(w, h)
    print(bmi)

if __name__ == "__main__":
    main()




