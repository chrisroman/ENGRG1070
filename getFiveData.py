# TOOL TO EXTRACT DATA FROM THE 200, 400, AND 600 FIVE_C60 LAMMPSTRJ FILES
data = open('COF_Project/Five_C60/600.dump.lammpstrj', 'r')
new_data = open('COF_Project/Five_C60/positions_600.txt', 'w')

def getData(file) :
  i = 0 # Line number
  time = 1 # Timestamp it occurred
  for line in file :
    i += 1
    if i % 4875 >= 4870 :
      new_data.write(str(time) + " " + line[3: ])
    if i == 4874 :
      time += 1
      i = 0
  return

getData(data)
# DATA GETS WRITTEN IN THE FORM:
# time c60# id x y z
# time = time in pico seconds (ps)