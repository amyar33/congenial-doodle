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
    def drive(self, distance, time):
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
#Defined the SUV class that inherits from the car class
class SUV(car):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, capacity, fuel_type, cylinders, engine_type, material, wheel, model, year, color, differential_type, diff_lock):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, capacity, fuel_type, cylinders, engine_type, material, wheel, model, year, color)
    self.differential_type = differential_type # in string
    self.diff_lock = diff_lock # in string,it's a yes - no question
    def dor_dor(self,place):
        print('You are headed to',place)
        light_weight_car.drive(self)
        print('You have arrived at',place,', have fun :)')
    def offroad(self,differential_type,diff_lock):
        if differential_type == '4WD' or differential_type == 'AWD' and diff_lock == 'yes':
            print('You have an offroad capable SUV')
        if differential_type == '4WD' or differential_type == 'AWD' and diff_lock == 'no':
            print('Be careful while offroading')
        if differential_type == '2WD':
            print('Change your car if you want to go offroading') 
#Defined the airplane class that inherits from the vehicle class
class airplane(vehicle):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, capacity, fuel_type, cylinders, engine_type, material, wing_span, model, num_of_engines):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, capacity, fuel_type, cylinders, engine_type, material)
    self.wing_span = wing_span # in meters
    self.model = model # in string
    self.num_of_engines = num_of_engines # in integer
    self.flight_permission = False
    #Defined the methods
    def take_off(self,weather_condition,runway_clearence,airport):
        if weather_condition == 'clear' and runway_clearence == 'clear':
            print('You have permission to take off from',airport,'airport')
            self.flight_permission = True
            print('You are taking off')
        else:
            print("You don't have the permission to take off")
    def landing(self,weather_condition_2,runway_clearence_2,airport_2):
        if weather_condition_2 == 'clear' and runway_clearence_2 == 'clear':
            print('You have permission to land at',airport_2,'airport')
            self.flight_permission = True
            print('You are landing')
        else:
            print("You don't have the permission to land")
#Defined the fighter airplane class that inherits from the airplane class
class fighter_airplane(airplane):
    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, capacity, fuel_type, cylinders, engine_type, material, wing_span, model, num_of_engines, num_of_missiles, stealth):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, capacity, fuel_type, cylinders, engine_type, material, wing_span, model, num_of_engines)
    self.num_of_missiles = num_of_missiles # in integer
    self.current_speed = current_speed # in mach
    self.stealth = stealth # a yes-no question to see if the plane could be detected by radars or not
    #Defined the methods    
    def shoot_missile(self,missile_type):
        if self.num_of_missiles > 0:
            self.num_of_missiles -= 1
            print('You have shot a',missile_type,'missile')
        else:
            print("You don't have any missiles to shoot")
    def maneuver(self,maneuver_name):
        print('You did a',maneuver_name,'maneuver because a missile was shot at you')
    def breaking_sound_barrier(self,current_speed):
        if current_speed > max_speed:
            print("You can't go faster than your maximum speed")
        elif current_speed < max_speed and current_speed > 1:
            print('You have broken the sound barrier')
