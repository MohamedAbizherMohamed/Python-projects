import sys

# Accept x, y, and z as command - line arguments .
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Set expr to an expression which is True if each of x, y, and z is less than or equal to the sum
# of the other two , and False otherwise .
expr = x <= y + z and y <= x + z and z<= y + x

# Write expr to standard output .
print(expr)