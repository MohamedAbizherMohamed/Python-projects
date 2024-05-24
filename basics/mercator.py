import sys
import math

# Read the latitude and longitude from command-line arguments    
lat = float(sys.argv[1])
lng = float(sys.argv[2])

# Convert latitude from degrees to radians
latradians = math.radians(lat)

# Compute the Mercator projection
x = lng; y = math.log((1 + math.sin(latradians)) / (1 - math.sin(latradians))) / 2

# Print the x and y values
print(x, y)