#การสิบทอด

class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    pass;

class Car(Vehicle):
    pass;

class Van(Vehicle):
    pass;

pickup01 = Pickup()
pickup01.turnOnAirConditioner()

cars01 = Car()
cars01.turnOnAirConditioner()

Van01 = Van()
Van01.turnOnAirConditioner()

