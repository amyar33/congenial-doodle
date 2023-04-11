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
    def turning(self):
        print('The vehicle is turning')
    def moving_with_constant_speed(self):
        print('The vehicle is moving with constant speed')
    def burning_fuel(self):
        print('The vehicle is burning fuel')
        
