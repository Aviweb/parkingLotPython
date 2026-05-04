from enum import Enum

class Size(Enum):
    SMALL="small"
    MEDIUM="medium"
    LARGE="large"

class VehicleType(Enum):
    CAR="car"
    BIKE="bike"
    BUS="bus"



class Vehicle():
    def __init__(self,size:Size,vehicle_type:VehicleType,number_plate:str):
        self.size=size
        self.vehicle_type=vehicle_type
        self.number_plate=number_plate

class Car(Vehicle):
    def __init__(self,size:Size,number_plate:str):
        super().__init__(size,VehicleType.CAR,number_plate)
        
        
car  = Car(Size.SMALL,"bwer")
print(car.size)
print(car.vehicle_type)
print(car.number_plate)