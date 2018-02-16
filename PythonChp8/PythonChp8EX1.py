
#Chapter 8 Exercise 1
#Armando Crews
#Exercise 1:
#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
#Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements



greeting = ['hey', 'hi', 'hello', 'sup', 'yo']

def chop(a):
  b = len(a)
  return a[1:b-1]
  
    
print (chop, greeting)
