class Car :
    wheels =4
    #constructor
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model 
    #method action
    def display_info(self):
        print(f"{self.brand}{self.model} has {self.wheels} wheels")
    
my_car = Car("Toyota","corolla")   
#calling method
my_car.display_info() 
#Car.display_info()