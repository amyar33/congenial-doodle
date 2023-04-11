#Made the vehicle class
class vehicle:
    #Defined the attributes
    def __init__(self,max_speed,weight,horsepower,fuel_type,cargo_capacity,passenger_capacity):
        self.max_speed = max_speed # in kilometers per hour
        self.weight = weight # in tons
        self.horsepower = horsepower # in hp
        self.fuel_type = fuel_type # in string
        self.cargo_capacity = cargo_capacity # in tons
        self.passenger_capacity = passenger_capacity # in integer
    #Defined the methods
    def acceleration(self):
        print('The vehicle is accelerating')
    def deceleration(self):
        print('The vehicle is decelerating')
    def turn(self):
        print('The vehicle is turning')
    def move_with_constant_speed(self):
        print('The vehicle is moving with constant speed')
    def burn_fuel(self):
        print('The vehicle is burning fuel')
#Defined the land_vehicle class that inherits from vehicle class
class land_vehicle(vehicle):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors):
        super().__init__(max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity)
        self.engine = engine
        self.num_of_doors = num_of_doors
    #Defined the methods
    def honk_the_horn(self):
        print('You are honking the horn')
    def start(self):
        print('You started the vehicle')
    def stop(self):
        print('You stopped the car')
    def open_door(self):
        print('You opened the door')
    def close_door(self):
        print('You closed the door')
    
