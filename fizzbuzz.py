####fizzbuss.py - fizzbuzz project with hardcoded values

n = 10
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