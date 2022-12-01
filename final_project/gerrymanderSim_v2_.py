import random


nation = []

print("How many democrats do you want to plot?")
dem_plots = int(input())
print("How many republicans do you want to plot?")
gop_plots = int(input())

print("How long do you want to create your nation?")
length = int(input())
print("How wide do you want to create the nation?")
width = int(input())

def setupNation(width,length):
	for i in range(0,width):
		nation.append([])
		for j in range(0,length):
			nation[i].append([])
	return nation

def copyList(list):
	secondList = []
	for i in range(0,len(list)):
		secondList.append([])
		for j in range(0,len(list[i])):
			secondList[i].append([])
	return secondList


def indexOrder(nation):
	duplicate = []
	duplicate = copyList(nation)
	for i in range(0,int(len(duplicate)/2)):
		for j in range(0,int(len(duplicate[i])/2)):
			duplicate[i][j] = f"nation[{i}][{j}]"
	return duplicate

def printNation(nation):
	for i in range(0,len(nation)-1):
		if (i%len(nation) == 0):
			print()
		else:
			print(nation[i])

def plotPartisanCities(dem_plots, gop_plots, nation):
	i = 0
	j = 0
	x = random.randint(0,length-1)
	y = random.randint(0,width-1)
	while (i <= dem_plots):
		#in case nation[x][y] is occupied, pick another spot to plot
		if (nation[x][y] == "D" or nation[x][y] == "R"):
			x = random.randint(0,length-1)
			y = random.randint(0,width-1)
		else:
			nation[x][y] = "D"
			i = i+1

	while (j <= gop_plots):
		#in case nation[x][y] is occupied, pick another spot to plot
		if (nation[x][y] == "D" or nation[x][y] == "R"):
			x = random.randint(0,length-1)
			y = random.randint(0,width-1)
			nation[x][y] = "R"
		else:
			nation[x][y] = "R"
		j = j+1

	return nation

def divideAndTally(nation):
	r = 0
	d = 0
	for i in range(0,int(len(nation)/2)-1):
		for j in range(0,int(len(nation[i])/2)-1):
			if nation[i][j] == "R":
				r = r + 1
			elif nation[i][j] == "D":
				d = d + 1

	return (r,d)


def main():
	_nation = []
	_order = []
	_nation = setupNation(width,length)
	_order = indexOrder(_nation)

	plotPartisanCities(dem_plots, gop_plots,_nation)
	printNation(_nation)

	x = divideAndTally(_nation)
	print(x)
	printNation(_order)

main()