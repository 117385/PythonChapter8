
#Python Chapter 8 Exercise 2
#Armando Crews
#Exercise 2: Figure out which line of the above program is still not properly guarded. See if you can construct a text file 
#which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it
#handles your new text file.


fhand = open('short.txt')
count = 0
for line in fhand:
    words = line.split()
    
    if len(words) == 0 : continue
    if words[0] != 'From': 
      continue
    if len(words) > 2:
      print(words[2])