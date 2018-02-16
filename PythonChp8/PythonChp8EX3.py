
#Python Chapter 8 Exercise 3
#Armando Crews
#Exercise 3: Rewrite the guardian code in the above example without two if statements. 
#Instead, use a compound logical expression using the and logical operator with a single if statement.

fhand = open('textfile.txt')
count = 0
for line in fhand:
    words = line.split()
    if (len(words) > 0) and (words[0] == 'From'): 
      print(words[2])
