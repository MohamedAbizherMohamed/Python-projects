import sys

# Accept weight ( float ) and height ( float ) as command - line arguments .
w = float(sys.argv[1])
h = float(sys.argv[2])

# Set bmi to weight divided by square of height .
bmi = w / (h * h)

# Print BMI value.
print(bmi)

