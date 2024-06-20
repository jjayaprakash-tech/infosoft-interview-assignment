"""
Script: fuel_station.py
Description: The FuelStation class is designed to manage fueling spots for three types of vehicles: Diesel, Petrol, and Electric.
Developer: Jayaprakash J
Date: June 21, 2024
"""

class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        # Initialize the total and available slots for each fuel type
        self.total_diesel = diesel
        self.available_diesel = diesel
        self.total_petrol = petrol
        self.available_petrol = petrol
        self.total_electric = electric
        self.available_electric = electric

    def fuel_vehicle(self, fuel_type: str) -> bool:
        # Check and allocate a spot for the specified fuel type
        if fuel_type == "diesel" and self.available_diesel > 0:
            self.available_diesel -= 1
            return True
        elif fuel_type == "petrol" and self.available_petrol > 0:
            self.available_petrol -= 1
            return True
        elif fuel_type == "electric" and self.available_electric > 0:
            self.available_electric -= 1
            return True
        else:
            return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        # Check and release a spot for the specified fuel type
        if fuel_type == "diesel" and self.available_diesel < self.total_diesel:
            self.available_diesel += 1
            return True
        elif fuel_type == "petrol" and self.available_petrol < self.total_petrol:
            self.available_petrol += 1
            return True
        elif fuel_type == "electric" and self.available_electric < self.total_electric:
            self.available_electric += 1
            return True
        else:
            return False

# Example usage:
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

# Test fueling vehicles and  opening slots
print(fuel_station.fuel_vehicle("diesel"))  # Expected: True  (1 slot now open)
print(fuel_station.fuel_vehicle("petrol"))  # Expected: True (1 slot now open)
print(fuel_station.fuel_vehicle("diesel"))  # Expected: True (0 slots now open)
print(fuel_station.fuel_vehicle("electric"))  # Expected: True (0 slots now open)
print(fuel_station.fuel_vehicle("diesel"))  # Expected: False  (0 slots open)
print(fuel_station.open_fuel_slot("diesel"))  # Expected: True (1 slot now open)
print(fuel_station.fuel_vehicle("diesel"))  # Expected: True  (0 slots now open)
print(fuel_station.open_fuel_slot("electric"))  # Expected: True (1 slot now open)
print(fuel_station.open_fuel_slot("electric"))  # Expected: False  (only 1 slot available at fuel station)
