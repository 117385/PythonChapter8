
#Python Chapter 8 Exercise 4
#Armando Crews
#Exercise 4: Write a program to open the file romeo.txt and read it line by line. For each line, 
#split the line into a list of words using the split function.

wordslist = []

input = input("Enter file name: ")
fileopen = open(input)

for line in fileopen:
	for word in line.split():
		if word not in wordslist:
			wordslist.append(word)

wordslist.sort()
print (wordslist)