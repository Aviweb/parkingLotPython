from enum import Enum
from typing import List
from datetime import datetime
import uuid


class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class VehicleType(Enum):
    CAR = "car"
    BIKE = "bike"
    BUS = "bus"


class Vehicle:
    def __init__(self, size: Size, vehicle_type: VehicleType, number_plate: str):
        self.size = size
        self.vehicle_type = vehicle_type
        self.number_plate = number_plate


class Car(Vehicle):
    def __init__(self, size: Size, number_plate: str):
        super().__init__(size, VehicleType.CAR, number_plate)


class Ticket:
    def __init__(self, parking_spot_id: str, number_plate: str):
        self.number_plate = number_plate
        self.parking_spot_id = parking_spot_id
        self.ticket_id = str(uuid.uuid4())
        self.entry_time = datetime.now()
        self.exit_time = None


class ParkingSpot:
    def __init__(self, spot_id, size: Size, is_empty=True):
        self.spot_id = spot_id
        self.size = size
        self.is_empty = is_empty


class Floor:
    def __init__(self, parking_spots: List[ParkingSpot]):
        self.parking_spots = parking_spots


class ParkingLotManagement:
    def __init__(self, floors: List[Floor]):
        self.floors = floors

    def findEmptySpot(self, size) -> ParkingSpot:
        for floor in self.floors:
            for spot in floor.parking_spots:
                if spot.is_empty and spot.size == size:
                    return spot
        return None

    def findSpotById(self, spot_id: str) -> ParkingSpot:
        for floor in self.floors:
            for spot in floor.parking_spots:
                if spot.spot_id == spot_id:
                    return spot
        return None

    def markSpot(self, parkingSpot: ParkingSpot, is_empty: bool):
        parkingSpot.is_empty = is_empty

    def generateTicket(self, parking_spot_id: str, number_plate: str) -> Ticket:
        return Ticket(parking_spot_id, number_plate)

    def parkVehicle(self, vehicle: Vehicle) -> Ticket:
        parking_spot = self.findEmptySpot(vehicle.size)

        if parking_spot:
            self.markSpot(parking_spot, False)
            return self.generateTicket(parking_spot.spot_id, vehicle.number_plate)

        return None

    def unparkVehicle(self, ticket: Ticket) -> bool:
        parking_spot = self.findSpotById(ticket.parking_spot_id)

        if parking_spot:
            self.markSpot(parking_spot, True)
            ticket.exit_time = datetime.now()
            return True

        return False


floor1 = [
    ParkingSpot(1, Size.SMALL, False),
    ParkingSpot(2, Size.SMALL, True),
    ParkingSpot(3, Size.SMALL, True)
]

floor2 = [
    ParkingSpot(4, Size.MEDIUM, True),
    ParkingSpot(5, Size.MEDIUM, True),
    ParkingSpot(6, Size.LARGE, True)
]

floors = [
    Floor(floor1),
    Floor(floor2)
]

parkingLotDemo = ParkingLotManagement(floors)