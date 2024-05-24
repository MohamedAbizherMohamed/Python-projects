import sys
import math

# Read command-line arguments for the coordinates of two points
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# Convert to radians
x1_rad = math.radians(x1)
x2_rad = math.radians(x2)
y1_rad = math.radians(y1)
y2_rad = math.radians(y2)

# Calculate the great-circle distance using the spherical law of cosines
d = 6359.83 * math.acos(math.sin(x1_rad) * math.sin(x2_rad) + 
                        math.cos(x1_rad) * math.cos(x2_rad) * 
                        math.cos(y1_rad - y2_rad))
                        


print(d)



