class Resident:
    def __init__(self, name, flat_number, maintenance_fee, status):
        self.name = name
        self.flat_number = flat_number
        self.maintenance_fee = maintenance_fee
        self.status = status.lower()

    def display_details(self):
        print(f"Resident Name: {self.name}")
        print(f"Flat Number: {self.flat_number}")
        print(f"Maintenance Fee: ₹{self.maintenance_fee:.2f}")
        print(f"Maintenance Status: {self.status.title()}")


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

    def display_all_maintenance_details(self):
        if not self.residents:
            print("No resident records found.")
            return

        print("Apartment Maintenance Records")
        print("-" * 32)
        for resident in self.residents:
            resident.display_details()
            print("-" * 32)


# Example usage
society = Society()

society.add_resident(Resident("Janhavi Dorge", "B-301", 2500, "paid"))
society.add_resident(Resident("Saee Thorat", "B-704", 2500, "pending"))

society.display_all_maintenance_details()