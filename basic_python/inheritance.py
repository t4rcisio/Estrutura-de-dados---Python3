class Vehicle:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def getBrand(self):
        return self.brand
    
    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

class Car(Vehicle):
    def __init__(self, vehicle, l_plate):
        Vehicle.__init__(self, vehicle.getBrand(), vehicle.getModel(), vehicle.getColor())
        self.l_plate = l_plate

    def getCarDescription(self):
        print("----------------------")
        print("Model: %s"         % self.getModel())
        print("Brand: %s"         % self.getBrand())
        print("Color: %s"         % self.getColor())
        print("License plate: %s" % self.l_plate)
        print("----------------------")


my_vehicle = Vehicle("Fiat", "uno", "red")
print(my_vehicle.getBrand())
print(my_vehicle.getModel())
print(my_vehicle.getColor())

my_car = Car(my_vehicle, "HJ0J56")
my_car.getCarDescription()


 