#Made the vehicle class
class vehicle:
    #Defined the attributes
    def __init__(self,max_speed,weight,horsepower,fuel_type,cargo_capacity,passenger_capacity,engine):
        self.max_speed = max_speed # in kilometers per hour
        self.weight = weight # in tons
        self.horsepower = horsepower # in hp
        self.fuel_type = fuel_type # in string
        self.cargo_capacity = cargo_capacity # in tons
        self.passenger_capacity = passenger_capacity # in integer
        self.engine = engine # in string
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
#Defined the land vehicle class that inherits from vehicle class
class land_vehicle(vehicle):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors):
        super().__init__(max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine)
        self.num_of_doors = num_of_doors # in integer
    #Defined the methods
    def honk_the_horn(self):
        print('You are honking the horn')
    def start(self):
        print('You started the vehicle')
    def stop(self):
        print('You stopped the vehicle')
    def open_door(self):
        print('You opened the door')
    def close_door(self):
        print('You closed the door')
#Defined the train class that inherits from the land vehicle class
class train(land_vehicle):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors, wagon, railway, train_station):
        super().__init__(max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors)
        self.wagon = wagon # in integer
        self.railway = railway # in string
        self.train_station = train_station # in string
    #Defined the methods
    def attach_wagon(self):
        self.wagon += 1
        print('You have attached a wagon')
    def detach_wagon(self):
        self.wagon -= 1
        print('You have detached a wagon')
    def change_railway(self):
        print('You have changed your railway')
    def arrive(self):
        print('You have arrived at the train station')
    def leave(self):
        print('You have left the train station')
#Defined the car class that inherits from the land vehicle class
class car(land_vehicle):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors, wheel, model, year):
        super().__init__(max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors)
        self.wheel = wheel # in integer
        self.model = model # in string
        self.year = year # in Gregorian year
        


