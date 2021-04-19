import random as ran   #importing random package
car=[1,9]   #creating list from 1 to 9 numbers randomly
#picked and printing this
try:
  num=ran.randint(car[0],car[-1])
  print("random number from ",car[0] ,"to",car[-1 ],"is",num)
  
except :#if an error occurres error message prints
  print("error")
