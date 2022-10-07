import re

def findFullySpelledName(line):
	pattern = r"([A-Z][a-z]+)"
	result = re.findall(pattern,line)
	return result

def findHonorNames(line):
	pattern = r"(Mr.)|(Mrs.)|(Ms.)|(Dr.).([A-Z][a-z]+).([A-Z][a-z]+)"
	result = re.findall(pattern,line)
	return result

def findAbbreviatedFirst(line):
	pattern = r"([A-Z])/'.'/([A-Z][a-z]+)"
	result = re.findall(pattern,line)
	return result

# def findAbbreviatedLast(line):
# 	pattern = r""

# def convertListToString(parts):
# 	fullName = ''
# 	for i in range(0,len(parts)-1):
# 		fullName = fullName + parts[i]

# 	return fullName

f = open("names.txt")
for line in f.readlines():
	#print(line)
	#foundIt = findFullySpelledName(line)
	foundHonorified = findHonorNames(line)
	print(foundHonorified)
	# name = convertListToString(foundHonorified)
	# print(name)

	abbreviatedFirst = findAbbreviatedFirst(line)
	print(abbreviatedFirst)

	# if foundIt is not None:
	# 	print(foundIt)
	# 	print(f"Name found: "{foundIt})
	# elif foundInt is None:
	# 	foundIt = findHonorNames(line);