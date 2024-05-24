import sys
import math

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# Convert degrees to radians
x11 = math.radians(x1)
y11 = math.radians(y1)
x22 = math.radians(x2)
y22 = math.radians(y2)
    
# Compute the great-circle distance using the formula
d = 6359.83 * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11 - y22))
    
print(d)



