# The input data you require for your program is provided in text format.
# This data is comprised of lines, each of which represents a defibrillator.
# Each defibrillator is represented by the following fields:

#     A number identifying the defibrillator
#     Name
#     Address
#     Contact Phone number
#     Longitude (degrees)
#     Latitude (degrees)

# These fields are separated by a semicolon (;).

# Beware: the decimal numbers use the comma (,) as decimal separator. Remember
# to turn the comma (,) into dot (.) if necessary in order to use the data in
# your program.
 
# DISTANCE
# The distance d between two points A and B will be calculated using the
# following formula:
# x = (longitudeB - longitudeA) x cos((latitudeB + latitudeA) / 2)
# y = (latitudeB - latitudeA)
# d = sqrt(x² + y²) x 6371

# Note: In this formula, the latitudes and longitudes are expressed in radians.
# 6371 corresponds to the radius of the earth in km.

# The program will display the name of the defibrillator located the closest
# to the user’s position. This position is given as input to the program.


from math import hypot, cos


def convert(coords):
    return [float(c.replace(',', '.')) for c in coords]


A = convert(input() for _ in range(2))
defibs = {}

for i in range(int(input())):
    _, nameB, _, _, *B  = input().split(';')
    B = convert(B)
    x = (B[0] - A[0]) * cos((A[1] + B[1]) / 2)
    y = B[1] - A[1]
    d = hypot(x, y) * 6371
    defibs[d] = nameB

print(defibs[min(defibs)])
