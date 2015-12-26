from attempt4 import *

file = open('COF_Project/Single_C60/200.dump.bucky.txt', 'r')
segments = open('COF_Project/Single_C60/points-200.txt', 'w')

points = diffCoeff(file)
for p in points :
  segments.write(str(p) + "\n")


file.close()