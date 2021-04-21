#python 3.7.1

#creating class library declaring a variable/function
class library:
  def __init__(self,a):#self is the instance for this constructor
#by using this self instance we can access attributes/methods under this method
    self.x=a;
    print(self.x)
    
  def sample(self,b):
    self.y=b
    print(self.y)
  
p=library("init constructor")
p. sample("normal function")
