#python 3.7.1

spam=5         #global variable
def error():
  spam=6       #local variable
  print(spam,"local variable")
  
error()    #calling error() function
print(spam,"global variable") #printing global variable

#Global variable: This variable scope work in
#any where inside the program

#Local variable: This variable scope work in
#the block of code only,not worked outside of 
#block
