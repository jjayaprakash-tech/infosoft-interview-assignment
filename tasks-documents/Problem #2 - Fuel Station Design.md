### Problem #2 - Fuel Station Design.md

### FuelStation Class Documentation

#### Overview
The `FuelStation` class is designed to manage fueling spots for three types of vehicles: Diesel, Petrol, and Electric. It allows vehicles to be fueled based on the availability of spots and provides methods to check and allocate spots (`fuel_vehicle`) as well as release them (`open_fuel_slot`).

#### Class Structure

```python
class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        """
        Initializes a FuelStation object with specific number of spots for each fuel type.

        Parameters:
        - diesel (int): Number of spots for Diesel vehicles.
        - petrol (int): Number of spots for Petrol vehicles.
        - electric (int): Number of spots for Electric vehicles.
        """
        self.total_diesel = diesel
        self.available_diesel = diesel
        self.total_petrol = petrol
        self.available_petrol = petrol
        self.total_electric = electric
        self.available_electric = electric
```

#### Explanation:
- **`__init__` method:** This constructor initializes a `FuelStation` object with parameters `diesel`, `petrol`, and `electric`, which represent the total number of spots available for each respective fuel type (`total_diesel`, `total_petrol`, `total_electric`). Initially, all spots are available (`available_diesel`, `available_petrol`, `available_electric`).

##### Methods

##### 1. `fuel_vehicle` Method

```python
    def fuel_vehicle(self, fuel_type: str) -> bool:
        """
        Allocates a fuel slot for a vehicle of specified fuel type.

        Parameters:
        - fuel_type (str): Type of fuel ("diesel", "petrol", or "electric").

        Returns:
        - bool: True if a slot was successfully allocated, False otherwise.
        """
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
```

#### Explanation:
- **`fuel_vehicle` method:** This method attempts to allocate a fuel slot for a vehicle of the specified `fuel_type`. It checks if there are available slots (`available_diesel`, `available_petrol`, `available_electric`) and reduces the count of available slots by one if available. Returns `True` if a slot was successfully allocated, otherwise `False`.

##### 2. `open_fuel_slot` Method

```python
    def open_fuel_slot(self, fuel_type: str) -> bool:
        """
        Releases a fuel slot for a vehicle of specified fuel type.

        Parameters:
        - fuel_type (str): Type of fuel ("diesel", "petrol", or "electric").

        Returns:
        - bool: True if a slot was successfully released, False otherwise.
        """
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
```

#### Explanation:
- **`open_fuel_slot` method:** This method releases a fuel slot of the specified `fuel_type`, provided there are slots that are currently occupied (`available_diesel`, `available_petrol`, `available_electric` less than `total_diesel`, `total_petrol`, `total_electric` respectively). It increments the count of available slots by one if a slot was successfully released. Returns `True` if a slot was successfully released, otherwise `False`.

##### Example Usage

```python
# Example usage of the FuelStation class
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
```

#### Explanation of Example Usage:
- Creates a `FuelStation` object with 2 spots for Diesel, 2 spots for Petrol, and 1 spot for Electric vehicles.
- Tests the `fuel_vehicle` method to allocate spots for different vehicle types and verifies if spots are correctly allocated or not.
- Tests the `open_fuel_slot` method to release spots and verifies if spots are correctly released or not.

#### Summary
The `FuelStation` class provides a straightforward implementation to manage and allocate fueling spots based on the type of vehicle. It ensures that only vehicles of the corresponding fuel type can use the allocated spots and provides methods to check availability and manage spot occupancy efficiently.


#### Source Code

The source code for the `FuelStation` classes can be found in [calendar.py](https://github.com/jjayaprakash-tech/infosoft-interview-assignment/blob/main/source-code/fuel_station.py).

#### Assignment Document

For the assignment details and requirements, refer to the [Assignment Document](https://github.com/jjayaprakash-tech/infosoft-interview-assignment/blob/main/assignment-documents).
