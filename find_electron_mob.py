# TOOL TO EXTRACT DATA FROM THE 200, 400, AND 600 FIVE_C60 LAMMPSTRJ FILES
# DATA GETS WRITTEN IN THE FORM:
# time c60# id x y z
# time = time in pico seconds (ps)


def getElectronMobility(file) :
  new_positions = {1: [], 2: [], 3: [], 4: [], 5: []}
  electron_mobs = []
  localEMob = []
  i = 0
  time = 1
  for line in file :
    i += 1 # Add one to the line number
    items = line.split(" ")
    c60_num = int(items[1])
    if i % 5 == 1 :
      new_positions[c60_num] = [float(items[3]), float(items[4]), float(items[5].strip())]
      if i != 1 :
        localEMob = []
        continue
    else :
      x = float(items[3])
      y = float(items[4])
      z = float(items[5].strip())
      new_positions[c60_num] = [x, y, z]
      deltaX = new_positions[c60_num][0] - new_positions[c60_num - 1][0]
      if abs(deltaX) >= 30 :
        deltaX = new_positions[c60_num][0] + 45.4624 - new_positions[c60_num - 1][0]
      deltaY = new_positions[c60_num][1] - new_positions[c60_num - 1][1]
      if abs(deltaY) >= 30 :
        deltaY = new_positions[c60_num][1] + 45.4624 - new_positions[c60_num - 1][1]
      deltaZ = new_positions[c60_num][2] - new_positions[c60_num - 1][2]
      if abs(deltaZ) >= 30 :
        deltaZ = new_positions[c60_num][2] + 51.75 - new_positions[c60_num - 1][2]
      eMob = ((deltaX**2 + deltaY**2 + deltaZ**2) ** (.5)) / 10
      electron_mobs.append(eMob)
  return electron_mobs

temperature = "600"
data = open('COF_Project/Five_C60/positions_%s.txt' %(temperature), 'r')
completed_data = open('COF_Project/Five_C60/electron_mobility-%s.txt' %(temperature), 'w')
# VALUES BASED ON THE TABLE GIVEN TO US IN THE PACKET
electron_transport = dict([(0.970609077, 293.5869317), (0.995118025, 126.3658863),(1.000613687, 100.0),
                           (1.018853671, 56.99443244), (1.067056986, 10.55990395), (1.116198719, 2.250353569),
                           (1.212357672, 0.058384391), (1.308134103, 0.000391313), (1.401857572, 0)])
distances = getElectronMobility(data)
# Made so that first array is all A to B, second is all B to C, and so on and so forth
# flipped = list(zip(*distances))
e_mobility = []
for i in range(len(distances)) :
  theKey = min(electron_transport.keys(), key=lambda x:abs(x-distances[i])) # Find the key value with the closest displacement to the one being compared
  value = electron_transport[theKey]
  e_mobility.append(value) # Append the corresponding electron mobility %
  completed_data.write(str(value) + "\n")

avgEMob = sum(e_mobility) / len(e_mobility)
print("AVG IS: %f%s" %(avgEMob, "%"))

data.close()
completed_data.close()