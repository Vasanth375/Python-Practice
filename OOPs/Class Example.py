class vehicle:
  name=""         #declaring 4 variables
  kind="car"
  colour=""
  value=100

  #uaing self parameter can we can access attributes
  #of that function only an instance is created for the class
  def description(self, name, colour, value):
    self.name=name
    self.colour=colour
    self.value=value

    desc_str="car details :- \n%s is %s of worth %.2f" % (self.name,self.colour,self.value)
    print(desc_str)
    
car1=vehicle()#creating object

#calling function(member function)
car1.description("Ford","dark silver",100000) 
