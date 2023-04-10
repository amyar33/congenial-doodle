#Made the vehicle class
class vehicle:
    def __init__(self,max_speed,weight,horsepower,fuel_type,cargo_capacity,passenger_capacity):
        self.max_speed = max_speed # in kilometers per hour
        self.weight = weight # in tons
        self.horsepower = horsepower # in hp
        self.fuel_type = fuel_type # in string
        self.cargo_capacity = cargo_capacity # in tons
        self.passenger_capacity = passenger_capacity # in integer
