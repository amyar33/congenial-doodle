#Made the engine class
class Engine:
    #Defined the attributes
    def __init__(self,capacity:float,fuel_type:str,cylinders:int,engine_type:str,material:str):
        self.capacity = capacity # in liters
        self.fuel_type = fuel_type # in string
        self.cylinders = cylinders # in integer
        self.engine_type = engine_type # in string
        self.material = material # in string
        self.running = False
    #Defined the methods
    def oil_change(self,oil_type):
        print("You have changed your engine's oil to ",oil_type)
    def cylinder_move(self):
        print('The cylinders are moving')
    def charge(self,watt):
        print('The engine is charging the battery with ',watt,' per hour')
    def start(self):
        if not self.running:
            self.running = True
            print('You started the engine')
        else:
            print('The engine is already running')
    def stop(self):
        if self.running:
            self.running = False
            print('You stopped the engine')
        else:
            print('The engine is already stopped')
#Made the vehicle class
class vehicle:
    #Defined the attributes
    def __init__(self,max_speed,weight,horsepower,cargo_capacity,passenger_capacity,capacity,fuel_type,cylinders,engine_type,material):
        self.max_speed = max_speed # in kilometers per hour
        self.weight = weight # in tons
        self.horsepower = horsepower # in hp
        self.cargo_capacity = cargo_capacity # in tons
        self.passenger_capacity = passenger_capacity # in integer
        self.engine = Engine(capacity, fuel_type, cylinders, engine_type, material)
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
    def drive(self):
        self.engine.start()
        self.acceleration()
        self.move_with_constant_speed()
        print('You are driving the vehicle')
#Defined the land vehicle class that inherits from vehicle class
class land_vehicle(vehicle):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity,capacity,fuel_type,cylinders,engine_type,material, num_of_doors,fuel_level):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity,capacity,fuel_type,cylinders,engine_type,material)
        self.num_of_doors = num_of_doors # in integer
        self.door_locked = True
        self.honk = False
        self.fuel_level = fuel_level
    #Defined the methods
    def honk_the_horn(self):
        if not self.honk:
            self.honk = True
            print('You are honking the horn')
            self.honk = False
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
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level,capacity,fuel_type,cylinders,engine_type,material ,wagon, railway, train_station):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors,fuel_level,capacity,fuel_type,cylinders,engine_type,material)
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
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level,capacity,fuel_type,cylinders,engine_type,material ,wheel, model, year, color):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level,capacity,fuel_type,cylinders,engine_type,material)
        self.wheel = wheel # in integer
        self.model = model # in string
        self.year = year # in Gregorian year
        self.color = color # in string
        self.hand_brake = True
        self.gear = 1 # in integer
    #Defined the methods
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
#Defined the truck class that inherits from the car class
class truck(car):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, capacity, fuel_type, cylinders, engine_type, material, wheel, model, year, color, cargo_type):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, capacity, fuel_type, cylinders, engine_type, material, wheel , model, year, color)
        self.cargo_type = cargo_type # in string
        self.cargo = False
    def load_cargo(self,cargo_weight,cargo_type):
        if self.cargo:
            print('The truck is already loaded')
        else:
            self.cargo = True
            print('You have loaded ', cargo_weight,' tons of ',cargo_type)
            truck.drive(self)
            print('You have arrived to your destination')
            truck.unload_cargo(self, cargo_weight, cargo_type)
    def unload_cargo(self,cargo_weight,cargo_type):
        if self.cargo:
            self.cargo = False
            print('You have unloaded',cargo_weight,'tons of',cargo_type)
        else:
            print('You have already unloaded the cargo')
#Defined the light weight class that inherits from the car class
class sedan(car):
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, capacity, fuel_type, cylinders, engine_type, material, wheel, model, year, color):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, capacity, fuel_type, cylinders, engine_type, material, wheel, model, year, color)
    def dor_dor(self,place):
        print('You are headed to',place)
        light_weight_car.drive(self)
        print('You have arrived at',place,', have fun :)')
