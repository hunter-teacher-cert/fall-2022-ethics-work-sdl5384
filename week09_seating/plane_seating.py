import random

seats = []
partiesRejected = 0

def setupSeats(row_length, column_length):
	for i in range(0,column_length):
		seats.append([])
		for j in range(0,row_length):
			seats[i].append([])
	return seats

def setupAsAvailable(seats):
	for i in range(0,len(seats)):
		for j in range(0, len(seats[i])):
			seats[i][j] = "avail"
	return seats

def displayPlaneStatus(seats):
	for i in range(0,len(seats)):
		print(seats[i])

def identifyAdjacentSeats(numberRequired,seats):
	#search for required number of seats for party in question
	#if number of seats is not available, say so
	i = 0
	j = 0
	index = 0
	enoughSeatsExist = True
	while(enoughSeatsExist and i < len(seats) and i < len(seats[0])):
		setupAsAvailableInRow = find_empty_seats(seats,i)
		print(len(seats))
		if (setupAsAvailableInRow == 0 or setupAsAvailableInRow < numberRequired):
			print("There are no consecutive seats available for this party.")
			enoughSeatsExist = False
		elif setupAsAvailableInRow >= numberRequired:
			seats[i][j] = "eco"
		i = i + 1

		return enoughSeatsExist

def totalAvailableSeats(seats):
	totalSeats = 0
	for i in range(0,len(seats)-1):
		totalSeats = totalSeats + find_empty_seats(seats,i)

	return totalSeats

def fillUpSeats(seats):
	#randomly pick a number of seats to fill
	#pick two random indices
	x = random.randint(0,len(seats)-1)
	y = random.randint(0,len(seats[0])-1)

	#assumption 65% of all passengers fly solo
	#the rest are parties of 2 or more
	totalEmptySeats = totalAvailableSeats(seats)
	while (totalEmptySeats > 0):
		randomVal = random.randint(1,100)
		if (randomVal < 66):
			#if seats[x][y] is not available, pick another seat
			if (seats[x][y] != "avail"):
				x = random.randint(0,len(seats)-1)
				y = random.randint(0,len(seats[0])-1)
				seats[x][y] = "eco_plus"
			else:
				seats[x][y] = "eco_plus"
			totalEmptySeats = totalEmptySeats - 1
		elif (67 <= randomVal < 100):
			partySize = random.randint(2,4)
			print(f"Party size: {partySize}")
			seatsFound = identifyAdjacentSeats(partySize,seats)
			if seatsFound is True:
				totalEmptySeats = totalEmptySeats - partySize
		#print(randomVal)

	#search through plane to see if there are seats available for party in question

def find_empty_seats(seats,row_number):
	emptySeats = 0
	for i in range(0,len(seats[row_number])):
		if (seats[row_number][i] == "avail"):
			emptySeats = emptySeats + 1

	return emptySeats

def main():
	plane = setupSeats(6,10)
	plane = setupAsAvailable(plane)
	howManySeats = find_empty_seats(plane,3)
	fillUpSeats(plane)
	displayPlaneStatus(seats)


main()
