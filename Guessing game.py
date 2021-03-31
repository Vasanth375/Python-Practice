#Program to find a guessing number
import random

print("Now your playing a Guessing game\n")

#initializing a random integer from 1 to 10
secretnum=random.randint(1,10)

print("You had only 5 chances\n")
for Guess in range(1,6):
  print("take a number guess from 1 to 10")
  
  #try and except block is to find if user entered any noninteger value
  try:
    guessnum=int(input())
    #guessnum=7
  except:
    print("not a valid input \n")
    
  """guessing number is greater than secret number 
  it prints too high"""
  if(guessnum>secretnum):
    print("too high")
  elif(guessnum<secretnum):
    print("too low")
  else:
    break     # this comdition comes when the 
              # guess is equal to secret number

if(guessnum==secretnum):
    print("Your guess is correct.You guessed number in "+str(Guess)+" chances")
else:
  print("Failed(≧▽≦)")
  print("You didn't entered correct number")
