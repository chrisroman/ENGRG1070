from findDiffCoeff import *

file = open('COF_Project/Single_C60/400.dump.bucky.txt', 'r')
segments = open('COF_Project/Single_C60/points-400.txt', 'w')

points = diffCoeff(file)
for p in points :
  segments.write(str(p) + "\n")


file.close()