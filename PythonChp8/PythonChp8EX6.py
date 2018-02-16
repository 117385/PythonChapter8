
#Python Chapter 8 Exercise 6
#Armando Crews 
#Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum 
#of the numbers at the end when the user enters "done". Write the program to store the numbers 
#the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

values = []
Still_Going = True

while Still_Going:
  newIn = input("Enter a number: \n")
  if newIn == "done":
    break
  else: 
    newIn = int(newIn)
    values.append(newIn)
    
print("The maximum value is: " + str(max(values)))
print("The minimum value is: " + str(min(values)))