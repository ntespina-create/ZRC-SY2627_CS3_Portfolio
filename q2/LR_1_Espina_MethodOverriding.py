class patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        discount = 0.2  
        return self.get_bill_amount() * (1 - discount)

class PhilHealthPatient(patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        discount = 0.15  
        return self.get_bill_amount() * (1 - discount)

regular_patient = patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("----------------------")

print("Patient name:", regular_patient.get_name())
print("Original Bill:", regular_patient.get_bill_amount())
print("Final Bill:", regular_patient.calculate_bill())

print("Patient name:", senior_patient.get_name())
print("Senior Bill:", senior_patient.get_bill_amount())
print("Final Bill:", senior_patient.calculate_bill())

print("Patient name:", philhealth_patient.get_name())
print("PhilHealth Bill:", philhealth_patient.get_bill_amount())
print("Final Bill:", philhealth_patient.calculate_bill())