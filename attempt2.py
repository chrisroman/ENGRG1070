# Formula for diffusion coefficient:
#     <[r(t0 + t) - r(t0)]^2>
# D = -----------------------
#              2t

# ONLY FOR Z
def diffCoeff(file) :
  z_curr = 0
  z_next = 0
  index = 0
  sq_dispList = []

  # Go through each line, save an index for the line
  for line in file :
    index += 1
    items = line.split(" ")
    if index % 1000 == 1 and index != 1  : # Using 10 runs, so split every 1000th line
      index = 1
    elif index == 10 :
      z_curr = float(items[4])    # Initialize values for z_curr and z_next
    elif index == 20 :
      z_next = float(items[4])          # Do stuff on the first run
      sq_disp = (z_next - z_curr) ** 2
      sq_dispList.append(sq_disp)
    else :
      if len(items) == 5 :
        z_curr = z_next          # Update the current one to z_next
        z_next = float(items[4]) # Update z_next to the actual next z_position
        sq_disp = (z_next - z_curr) ** 2
        sq_dispList.append(sq_disp)
  return sq_dispList
