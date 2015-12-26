from attempt3 import *

file = open('COF_Project/Single_C60/600.dump.bucky.txt', 'r')
segments = open('COF_Project/Single_C60/points-600.txt', 'w')

points = diffCoeff(file)
for p in points :
  segments.write(str(p) + "\n")


file.close()