from abc import ABC, abstractmethod
class DigitalScale(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def tare(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass


class ElectronicBalance(DigitalScale):
    def __init__(self):
        self.__tare_offset = 0.0  

    def power_on(self):
        print("Scale is ON.")

    def tare(self):
        self.__tare_offset = 50.0  
        print("Tare pressed: Beaker weight ignored (0.0g)")

    def get_weight(self):
        raw_load_cell = 55.25  
        final_grams = self.__calculate_grams(raw_load_cell)
        return final_grams

    def __calculate_grams(self, signal):
        return signal - self.__tare_offset


scale = ElectronicBalance()

print("--- Lab Digital Scale ---")
scale.power_on()
scale.tare()
print("[Display Screen] Weight:", scale.get_weight(), "g")
print("\n-------------------------\n")