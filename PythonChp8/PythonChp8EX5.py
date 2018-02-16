
#Python Chapter 8 Exercise 5
#Armando Crews
#Exercise 5: Write a program to read through the mail box data and when you find line that starts with "From", 
#you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.
#File name:short.txt

file = input("Enter a file name.")

fhand = open(file)

count = 0 

for line in fhand:
  words = line.split()
  if len(words) == 0 : continue
  if words[0] != 'From' : continue
  print(words[1])
  if words[0] == 'From' : 
    count = count + 1

print ("There were " + str(count) + " lines in the file with From as the first word.")