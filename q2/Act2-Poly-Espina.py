#A.
#Duck typing is a concept where Python focuses on an object's behavior (its methods and attributes) rather than its actual class type. If an object provides the required method, Python executes it without verifying class hierarchy or inheritance.
#B.
#It only needed to deifne the exact method being called that loop (like speak() or move())




class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:  
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)

#The function start_trip(vehicle) receives different objects and calls the same method name, move(). Despite Car, Boat, and Drone being unrelated classes without an inheritance hierarchy, each object responds using its own specific implementation.
