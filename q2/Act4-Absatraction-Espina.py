from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class  pHSensor(Sensor):
    def get_reading(self):
        return 7.2 

class TemperatureSensor(Sensor):
    def get_reading(self):
        return 24.5

p = pHSensor()
t = TemperatureSensor()

print("--- Lab Inventory System ---")
print("[pH Sensor] Reading: ", p.get_reading(), "pH (Neutral)")
print("[Temperature Sensor] Reading: ", t.get_reading(), "°C")
print("\n----------------------------\n")