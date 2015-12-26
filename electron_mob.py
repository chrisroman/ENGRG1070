# TOOL TO EXTRACT DATA FROM THE 200, 400, AND 600 FIVE_C60 LAMMPSTRJ FILES
# DATA GETS WRITTEN IN THE FORM:
# time c60# id x y z
# time = time in pico seconds (ps)


def getElectronMobility(file) :
  old_positions = {1: [], 2: [], 3: [], 4: [], 5: []}
  new_positions = {1: [], 2: [], 3: [], 4: [], 5: []}
  electron_mobs = []
  localEMob = []
  i = 0
  time = 1
  for line in file :
    if i % 5 == 0 and i <= 50: # If the last iteration was the 5th line
      electron_mobs.append(localEMob)
      localEMob = []
    i += 1 # Add one to the line number
    items = line.split(" ")
    c60_num = int(items[1])
    if i <= 5 : # First timestamp
      old_positions[c60_num] = [float(items[3]), float(items[4]), float(items[5].strip())]
    elif i <= 10 :
      new_positions[c60_num] = [float(items[3]), float(items[4]), float(items[5].strip())]      
      deltaX = new_positions[c60_num][0] - old_positions[c60_num][0]
      deltaY = new_positions[c60_num][1] - old_positions[c60_num][1]
      deltaZ = new_positions[c60_num][2] - old_positions[c60_num][2]
      eMob = (deltaX**2 + deltaY**2 + deltaZ**2) ** (.5)
      print(eMob)
      localEMob.append(eMob)
    elif i == 11 :
      print(old_positions)
      print(new_positions)
      break
    else :
      old_positions[c60_num] = new_positions[c60_num]
      new_positions[c60_num] = [float(items[3]), float(items[4]), float(items[5].strip())]
      deltaX = new_positions[c60_num][0] - old_positions[c60_num][0]
      deltaY = new_positions[c60_num][1] - old_positions[c60_num][1]
      deltaZ = new_positions[c60_num][2] - old_positions[c60_num][2]
      eMob = (deltaX**2 + deltaY**2 + deltaZ**2) ** (.5)
      localEMob.append(eMob)
  return electron_mobs


data = open('COF_Project/Five_C60/positions_200.txt', 'r')
eMobs = getElectronMobility(data)
for thing in eMobs :
  print(thing)