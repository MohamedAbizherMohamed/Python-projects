import sys

# Command line arguements
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Calculate the day of the week using Zeller's Congruence
y0 = y - (14 - m) // 12
x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
dow = (d + x0 + 31 * m0 // 12) % 7

# Map the numbers to the actual days of the week
dowlist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Print the day of the week
print(dowlist[dow])