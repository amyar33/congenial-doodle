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
    def __init__(self, max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors,fuel_level):
        super().__init__(max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine)
        self.num_of_doors = num_of_doors # in integer
        self.running = False
        self.door_locked = True
        self.honk = False
        self.fuel_level = fuel_level
    #Defined the methods
    def honk_the_horn(self):
        if not self.honk:
            self.honk = True
            print('You are honking the horn')
            self.honk = False
    def start(self):
        if not self.running:
            self.running = True
            print('You started the vehicle')
        else:
            print('The vehicle is already running')
    def stop(self):
        if self.running:
            self.running = False
            print('You stopped the vehicle')
        else:
            print('The vehicle is already stopped')
    def open_doors(self):
        if self.door_locked:
            self.door_locked = False
            print('You opened the doors')
        else:
            print('The doors are already open')
    def close_doors(self):
        if not self.door_locked:
            self.door_locked = True
            print('You closed the door')
        else:
            print('The doors are already locked')
    def refuel(self):
        if self.fuel_level < 100:
            self.fuel_level = 100
            print('The vehicle is refueled')
#Defined the train class that inherits from the land vehicle class
class train(land_vehicle):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors, fuel_level, wagon, railway, train_station):
        super().__init__(max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors,fuel_level)
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
    def change_railway(self,rail_name):
        print('You have changed your railway to ', rail_name)
    def arrive(self,station_name):
        print('You have arrived at ',station_name,' train station')
    def leave(self,station_name):
        print('You have left ',station_name,' train station')
#Defined the car class that inherits from the land vehicle class
class car(land_vehicle):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors, fuel_level, wheel, model, year, color):
        super().__init__(max_speed, weight, horsepower, fuel_type, cargo_capacity, passenger_capacity, engine, num_of_doors, fuel_level)
        self.wheel = wheel # in integer
        self.model = model # in string
        self.year = year # in Gregorian year
        self.color = color # in string
        self.hand_brake = True
        self.gear = 1 # in integer
    def pull_hand_brake(self):
        if self.hand_brake:
            print('The hand brake is already pulled')
        else:
            self.hand_brake = True
            print('The hand brake is pulled')
    def realese_hand_brake(self):
        if self.hand_brake:
            self.hand_brake = False
            print('The hand brake is realesed')
        else:
            print('The hand brake is already realesed')
    def gear_up(self):
        self.gear += 1
        print('You have geared up to ',self.gear,' gear')
    def gear_down(self):
        if self.gear == 1:
            print('You are at the 1st gear and can not gear down')
        else:
            self.gear -= 1
            print('You have geared down to ',self.gear,' gear')

