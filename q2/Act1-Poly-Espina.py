class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    # Getters and setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    # Base methods
    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80  # 20% discount

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85  # 15% discount

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


# Testing matching the exact module sample output format
print("Hospital Billing System\n")

p1 = Patient("Juan Dela Cruz", 15000.00)
print(f"Patient Name: {p1.get_name()}")
p1.display_patient_type()
print(f"Original Bill: P{p1.get_bill_amount():,.2f}")
print(f"Final Bill: P{p1.calculate_bill():,.2f}\n")

p2 = SeniorPatient("Maria Santos", 15000.00)
print(f"Patient Name: {p2.get_name()}")
p2.display_patient_type()
print(f"Original Bill: P{p2.get_bill_amount():,.2f}")
print(f"Final Bill: P{p2.calculate_bill():,.2f}\n")

p3 = PhilHealthPatient("Pedro Reyes", 15000.00)
print(f"Patient Name: {p3.get_name()}")
p3.display_patient_type()
print(f"Original Bill: P{p3.get_bill_amount():,.2f}")
print(f"Final Bill: P{p3.calculate_bill():,.2f}")
