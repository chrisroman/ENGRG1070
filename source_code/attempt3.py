# Formula for diffusion coefficient:
#     <[r(t0 + t) - r(t0)]^2>
# D = -----------------------
#              2t

# ONLY FOR Z
def diffCoeff(file) :
  z_init = 0
  z_next = 0
  index = 0
  sq_dispList = []

  # Go through each line, save an index for the line
  for line in file :
    index += 1
    items = line.split(" ")
    if index == 10 :
      z_init = float(items[4])    # Initialize values for z_init and z_next
    elif index == 20 :
      z_next = float(items[4])          # Do stuff on the first run
      sq_disp = (z_next - z_init) ** 2
      sq_dispList.append(sq_disp)
    else :
      if len(items) == 5 :
        z_next = float(items[4]) # Update z_next to the actual next z_position
        sq_disp = (z_next - z_init) ** 2
        sq_dispList.append(sq_disp)
  return sq_dispList
