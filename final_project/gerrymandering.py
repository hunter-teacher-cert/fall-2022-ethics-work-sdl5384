import random

# get you some user input for great justice!
dem_plots = int(input("How many democrat centers do you want to plot? "))
gop_plots = int(input("How many republican centers do you want to plot? "))

length = int(input("How long do you want to create your nation? "))
width = int(input("How wide do you want to create the nation? "))



def setupNation(width, length):
  '''
  Builds a square nation in the form of a 2d array.
  This nation is unpopulated, as is denoted by the default value
  of " "
  '''
  nation = []
  for i in range(0, width):
    nation.append([])
    for j in range(0, length):
      nation[i].append(" ")

  return nation



def printNation(nation):
  '''
  just a 2d array print fxn. Sure would be great if python had one.
  '''
  for i in range(len(nation)):
    print(nation[i])

def plotPartisanCities(dem_plots, gop_plots, nation):
  '''
  puts plots of population hubs (assumed to be equal in size)
  of a given party affiliation on a 2d map of a square nation
  plots dems as D and pubs as R
  '''

  while(dem_plots > 0):
    x = random.randint(0, length-1)
    y = random.randint(0, length-1)
    
    if(nation[x][y] == " "):
      nation[x][y] = "D"
      dem_plots = dem_plots -1
    
    
  while(gop_plots > 0):
    x = random.randint(0, length-1)
    y = random.randint(0, length-1)
    
    if(nation[x][y] == " "):
      nation[x][y] = "R"
      gop_plots = gop_plots -1 



def horiMander(nation):
  '''
  models a possable gerymandering result via just doing
  horizontal slices.
  '''
  rDis = 0
  dDis = 0
  purple = 0
  for i in range(len(nation)):
    r = 0
    d = 0
    for j in range(len(nation[i])):
      if nation[i][j] == "R":
        r = r + 1
      if nation[i][j] == "D":
        d = d + 1
    if r > d:
      rDis = rDis + 1
    elif r < d:
      dDis = dDis + 1
    else:
      purple = purple + 1

  print("In a Horizontal districting:")
  print("Number of republican districts: " + str(rDis))
  print("Number of democratic districts: " + str(dDis))
  print("Number of purple districts: " + str(purple))

def vertiMander(nation):
  '''
  models a possable gerymandering result via just doing
  Vertical slices.
  '''
  rDis = 0
  dDis = 0
  purple = 0
  rows = len(nation)
  cols = len(nation[0])

  for j in range(0, cols):
    r = 0
    d = 0
    for i in range(0, rows):
      if nation[i][j] == "R":
        r = r + 1
      if nation[i][j] == "D":
        d = d + 1
    if r > d:
      rDis = rDis + 1
    elif r < d:
      dDis = dDis + 1
    else:
      purple = purple + 1
      
  print("In a Vertical districting:")
  print("Number of republican districts: " + str(rDis))
  print("Number of democratic districts: " + str(dDis))
  print("Number of purple districts: " + str(purple))

def main():
  _nation = setupNation(width, length)

  print()
  plotPartisanCities(dem_plots, gop_plots, _nation)
  print('Raw nation output:')
  printNation(_nation)
  print()
  horiMander(_nation)
  print()
  vertiMander(_nation)
  

main()