import sys
import math

x1 = float(sys.argv[1])
x2 = float(sys.argv[2])
y1 = float(sys.argv[3])
y2 = float(sys.argv[4])

x1_rad = math.radians(x1)
x2_rad = math.radians(x2)
y1_rad = math.radians(y1)
y2_rad = math.radians(y2)

d = 6359.83 * math.arccos((math.sin(x1_rad) * math.sin(x2_rad)) + (math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad -y2_rad)))


print(d)