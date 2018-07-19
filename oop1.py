class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
        print("Creted an instance of {} , {}".format(self.make,self.model))
    def start_the_car(self):
        print("Started the car {} , {}".format(self.make,self.model))
    def set_year(self,year):
        self.year=year
        print("The year of {} - {}  is {}".format(self.make,self.model,self.year))
    def set_current_location(self,current_location):
        self.current_location=current_location
        print("The {} - {}  is now at {}".format(self.make,self.model,self.current_location))

c1=Car("Honda","CRV")    
c2=Car("Honda","Accord")

c1.start_the_car()
c2.start_the_car()

c1.set_year("2008")
c2.set_year("2007")

c1.set_current_location("Houston")
c2.set_current_location("Austin")