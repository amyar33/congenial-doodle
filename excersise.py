#Made the engine class
class Engine:

    #Defined the attributes
    def __init__(self,engine_capacity:float,fuel_type:str,cylinders:int,engine_type:str,engine_material:str):
        self.engine_capacity = engine_capacity # in liters
        self.fuel_type = fuel_type # in string
        self.cylinders = cylinders # in integer
        self.engine_type = engine_type # in string
        self.engine_material = engine_material # in string
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
    def __init__(self,max_speed,weight,horsepower,cargo_capacity,passenger_capacity,engine_capacity,fuel_type,cylinders,engine_type,engine_material):
        self.max_speed = max_speed # in kilometers per hour
        self.weight = weight # in tons
        self.horsepower = horsepower # in hp
        self.cargo_capacity = cargo_capacity # in tons
        self.passenger_capacity = passenger_capacity # in integer
        self.engine = Engine(engine_capacity, fuel_type, cylinders, engine_type, engine_material)

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
        speed = distance / time
        print('You are driving the vehicle with constant speed of',speed,'km/h')

#Defined the land vehicle class that inherits from vehicle class
class land_vehicle(vehicle):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity,engine_capacity,fuel_type,cylinders,engine_type,engine_material, num_of_doors,fuel_level):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity,engine_capacity,fuel_type,cylinders,engine_type,engine_material)
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
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level,engine_capacity,fuel_type,cylinders,engine_type,engine_material ,wagon, railway):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors,fuel_level,engine_capacity,fuel_type,cylinders,engine_type,engine_material)
        self.wagon = wagon # in integer
        self.railway = railway # in string

    #Defined the methods
    def attach_wagon(self):
        self.wagon += 1
        print('You have attached a wagon and currently have',self.wagon,'wagons attached')

    def detach_wagon(self):
        self.wagon -= 1
        print('You have detached a wagon and currently have',self.wagon,'wagons attached')

    def change_railway(self,rail_name):
        print('You have changed your railway to ',rail_name)

    def arrive(self,station_name):
        print('You have arrived at ',station_name,' train station')

    def leave(self,station_name):
        print('You have left ',station_name,' train station')

#Defined the car class that inherits from the land vehicle class
class car(land_vehicle):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level,engine_capacity,fuel_type,cylinders,engine_type,engine_material ,wheel, model, year, color):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level,engine_capacity,fuel_type,cylinders,engine_type,engine_material)
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
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wheel, model, year, color, cargo_type):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wheel , model, year, color)
        self.cargo_type = cargo_type # in string
        self.cargo = False

    #Defined the methods
    def load_cargo(self,cargo_weight,cargo_type,distance,time):
        if self.cargo:
            print('The truck is already loaded')
        else:
            self.cargo = True
            print('You have loaded ', cargo_weight,' tons of ',cargo_type)
            truck.drive(self,distance,time)
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

    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wheel, model, year, color):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wheel, model, year, color)
    
    #Defined the methods
    def dor_dor(self,place):
        print('You are headed to',place)
        vehicle.drive(self)
        print('You have arrived at',place,', have fun :)')

#Defined the SUV class that inherits from the car class
class SUV(car):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wheel, model, year, color, differential_type, diff_lock):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, num_of_doors, fuel_level, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wheel, model, year, color)
        self.differential_type = differential_type # in string
        self.diff_lock = diff_lock # in string,it's a yes - no question
    
    #Defined the methods
    def dor_dor(self,place,distance,time):
        print('You are headed to',place)
        vehicle.drive(self,distance,time)
        print('You have arrived at',place,', have fun :)')

    def offroad(self):
        if self.differential_type == '4WD' or self.differential_type == 'AWD' and self.diff_lock == 'yes':
            print('You have an offroad capable SUV')
        elif self.differential_type == '4WD' or self.differential_type == 'AWD' and self.diff_lock == 'no':
            print('Be careful while offroading')
        elif self.differential_type == '2WD':
            print('Change your car if you want to go offroading') 

#Defined the airplane class that inherits from the vehicle class
class airplane(vehicle):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wing_span, model, num_of_engines):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material)
        self.wing_span = wing_span # in meters
        self.model = model # in string
        self.num_of_engines = num_of_engines # in integer
        self.flight_permission = False

    #Defined the methods
    def take_off(self,weather_condition,runway_clearence,airport):
        if weather_condition == 'clear' and runway_clearence == 'clear':
            print('You have permission to take off from',airport,'airport')
            self.flight_permission = True
            print('You are taking off from',airport,'airport')
        else:
            print("You don't have the permission to take off")

    def landing(self,weather_condition_2,runway_clearence_2,airport_2):
        if weather_condition_2 == 'clear' and runway_clearence_2 == 'clear':
            print('You have permission to land at',airport_2,'airport')
            self.flight_permission = True
            print('You are landing at',airport_2,'airport')
        else:
            print("You don't have the permission to land")

#Defined the fighter airplane class that inherits from the airplane class
class fighter_airplane(airplane):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wing_span, model, num_of_engines, num_of_missiles):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wing_span, model, num_of_engines)
        self.num_of_missiles = num_of_missiles # in integer
        self.hourly_cost = 15000 # in dollars

    #Defined the methods    
    def shoot_missile(self):
        if self.num_of_missiles > 0:
            self.num_of_missiles -= 1
            print('You have shot a missile')
        else:
            print("You don't have any missiles to shoot")

    def maneuver(self,maneuver_name):
        print('You did a',maneuver_name,'maneuver because a missile was shot at you')

    def breaking_sound_barrier(self,current_speed):
        if current_speed > self.max_speed:
            print("You can't go faster than your maximum speed")
        elif current_speed < self.max_speed and current_speed > 1:
            print('You have broken the sound barrier')

#Defined the squadron class that has an aggrigation relationship with fighter airplanes
class squadron:
    def __init__(self,name,jets):
        #Defined the attributes of the class
        self.name = name # the name of the squadron, in string
        self.jets = jets # Use aggregation to create a list of fighter jet objects

    #Defined the methods
    def attack(self,target):
        print(self.name,'is attacking',target)

        for i in self.jets:
            fighter_airplane.shoot_missile

#Defined the passenger airplane class that inherits from the airplane class
class passenger_airplane(airplane):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wing_span, model, num_of_engines, ticket_price, flight_duration):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, wing_span, model, num_of_engines)
        self.ticket_price = ticket_price # in dollars
        self.flight_duration = flight_duration # in hours
        self.total_cost = 0
        self.hourly_cost = 3000 # in dollars

    #Defined the methods 
    def overboard_check(self,num_of_tickets):
        if num_of_tickets > self.passenger_capacity:
            num_of_penalty = num_of_tickets - self.passenger_capacity
            print('You have overboarded the airplane and have to pay fine to',num_of_penalty,'people')
            total_penalty = num_of_penalty * self.ticket_price * 1.2
            print('Your total penalty is:',total_penalty)

    def check_proftibility(self,num_of_tickets):
        if num_of_tickets > self.passenger_capacity:
            num_of_penalty = num_of_tickets - self.passenger_capacity
            total_penalty = num_of_penalty * self.ticket_price * 1.2 
            total_sell = self.passenger_capacity * self.ticket_price
            self.total_cost = (self.hourly_cost * self.flight_duration) + total_penalty
        else:
            total_sell = num_of_tickets * self.ticket_price
            self.total_cost = self.hourly_cost * self.flight_duration
        if total_sell > self.total_cost:
            profit = total_sell - self.total_cost
            print('The flight is profitable and has a profit of',profit,'dollars')
        else:
            loss = self.total_cost - total_sell
            print('The flight is not profitable and has a loss of',loss,'dollars')

#Defined the marine vehicle class that inherits from the vehicle class
class marine_vehicle(vehicle):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, crew_capacity):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material)
        self.crew = [] # initial crew is empty
        self.crew_capacity = crew_capacity # in integer

    #Defined the methods
    def hire_crew(self, name, role):
            # add a tuple of name and role to the crew list, if there is space available
            if len(self.crew) < self.crew_capacity:
                self.crew.append((name, role))
                return True # hiring successful
            else:
                return False # hiring failed

    def fire_crew(self, name):
            # remove a tuple of name and role from the crew list, if it exists
            for i in range(len(self.crew)):
                if self.crew[i][0] == name:
                    self.crew.pop(i)
                    return True # firing successful
            return False # firing failed

#Defined the cruise ship class that inherits from the marine vehicle class
class cruise_ship(marine_vehicle):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, crew_capacity):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, crew_capacity)
        # initialize an empty dictionary to store the passengers
        self.passengers = {}

    #Defined the methods
    def book_passenger(self, name, cabin):
        # check if the cabin is available and the passenger is not already booked
        if cabin not in self.passengers and name not in self.passengers.values():
            # add the passenger name and cabin number to the dictionary
            self.passengers[cabin] = (name, False) # False means not checked in
            return True # booking successful
        else:
            return False # booking failed

    def cancel_passenger(self, name):
        # check if the passenger is booked
        if name in self.passengers.values():
            # find the cabin number of the passenger
            for cabin in self.passengers:
                if self.passengers[cabin][0] == name:
                    # remove the passenger name and cabin number from the dictionary
                    self.passengers.pop(cabin)
                    return True # cancellation successful
        return False # cancellation failed

    def check_in_passenger(self, name):
        # check if the passenger is booked and not checked in
        if name in self.passengers.values():
            for cabin in self.passengers:
                if self.passengers[cabin][0] == name and not self.passengers[cabin][1]:
                    # update the checked_in attribute to True
                    self.passengers[cabin] = (name, True)
                    return True # check-in successful
        return False # check-in failed

    def check_out_passenger(self, name):
        # check if the passenger is booked and checked in
        if name in self.passengers.values():
            for cabin in self.passengers:
                if self.passengers[cabin][0] == name and self.passengers[cabin][1]:
                    # update the checked_in attribute to False
                    self.passengers[cabin] = (name, False)
                    return True # check-out successful
        return False # check-out failed

#Defined the submarine class that inherits from the marine vehicle class
class submarine(marine_vehicle):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, crew_capacity, max_depth, max_torpedoes):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, crew_capacity)
        self.max_depth = max_depth # in meters
        self.depth = 0 # initial depth is zero
        self.max_torpedoes = max_torpedoes # in integers
    
    #Defined the methods
    def dive(self, depth):
        # check if the depth is within the range of 0 to max_depth
        if 0 <= depth <= self.max_depth:
            self.depth = depth
            return True 
        else:
            return False
    
    def surface(self):
        # set the depth attribute to zero
        self.depth = 0

    def fire_torpedoe(self, target):
        # check if the submarine has any torpedoes left
        if self.torpedoes > 0:
            # simulate firing a torpedo at a target
            print("You fired a torpedo at",target)
            # decrease the number of torpedoes by one
            self.torpedoes -= 1
            return True # firing successful
        else:
            return False # firing failed
    
    def reload_torpedoe(self):
        # check if the number of torpedoes is below the max_torpedoes
        if self.torpedoes < self.max_torpedoes:
            # increase the number of torpedoes by one
            self.torpedoes += 1
            return True # reloading successful
        else:
            return False # reloading failed

#Defined the aircraft carrier class that inherits from the marine vehicle class
class aircraft_carrier(marine_vehicle):

    #Defined the attributes that were not defined in the super class
    def __init__(self, max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, crew_capacit, aircraft_capacity):
        super().__init__(max_speed, weight, horsepower, cargo_capacity, passenger_capacity, engine_capacity, fuel_type, cylinders, engine_type, engine_material, crew_capacity)
        # initialize an empty list to store the aircrafts
        self.aircrafts = []
        self.aircraft_capacity = aircraft_capacity
    
    #Defined the methods
    def launch_aircraft(self, name):
        # check if the aircraft is on board and ready to launch
        if name in self.aircrafts:
            # remove the aircraft name from the list
            self.aircrafts.remove(name)
            return True # launching successful
        else:
            return False # launching failed
    
    def land_aircraft(self, name):
        # check if the aircraft is not on board and there is space available
        if name not in self.aircrafts and len(self.aircrafts) < self.aircraft_capacity:
            # add the aircraft name to the list
            self.aircrafts.append(name)
            return True # landing successful
        else:
            return False # landing failed