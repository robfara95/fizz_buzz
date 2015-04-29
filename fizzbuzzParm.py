####fizzbuzzParm.py - fizzbuzz project entering max number on screen

import sys

if len(sys.argv) == 1:
  inputNumber = raw_input("Enter maximum number for Fizz Buzz: ")
else:
  inputNumber = sys.argv[1]

hasValidNumEntered = False  
  
while not hasValidNumEntered:
  try:
    n = int( inputNumber)
    hasValidNumEntered = True 
  except ValueError:
    inputNumber = raw_input("Enter maximum number for Fizz Buzz: ")

##n = int(sys.argv[1])  
print ("Fizz Buzz counting up to {0}".format(n))

for i in range(1,n+1):
  
  if i % 3 == 0 and i % 5 == 0:
    print 'fizzbuzz'    
  elif i % 3 == 0:
    print "fizz"
  elif i % 5 == 0:
    print "buzz"
  else :
    print(i)