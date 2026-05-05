from enum import Enum
from typing import List

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

class ParkingSpot():
    def __init__(self,spot_id,is_empty):
        self.spot_id=spot_id
        self.is_empty=is_empty

class Floor():
    def __init__(self,parking_spots:List[ParkingSpot]):
        self.parking_spots=parking_spots
        

class ParkingLotManagement():
    def __init__(self,floors:List[Floor]):
        self.floors=floors
    
    def findSpot(self,size)->str:
        for floor in self.floors:
            for spot in floor:
                if(spot.is_empty):
                    return spot.spot_id

floor1=[ParkingSpot(i+1,False) if i==0 else ParkingSpot(i+1,True) for i in range(3)]
floor2=[ParkingSpot(i+1,False) for i in range(3)]

floor1[2].is_empty=True

floors=[floor1,floor2]
    
parkingLotDemo=ParkingLotManagement(floors)
print(parkingLotDemo.findSpot("small"))
        