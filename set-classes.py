# examples

vo = {
    'stock_number': 'XS28021',
    'vin': 'CWQSD232978983',
    'licence_plate': '123-DE-123',
    'emplacement_file': 'B1',
    'emplacement_zone': 'stockage',
    'changelog': [("in_LC", "2020-11-20 09:57"), ("in_ZoneStockage", "2020-11-20 09:57")]
}

file = {
    'nom_file': 'B1',
    'capacite_max': 5,
    'occupation': 3
}

user = {
    'prenom': "jean",
    'nom': "dupont",
    'fonction': "jockey"
}

operations = {
    'stock_number_1': [("in_LC", "2020-11-26 09:57"), ("in_ZoneStockage", "2020-11-26 09:57")],
    'stock_number_2': [],
    'stock_number_3': [],
    'stock_number_4': [],
    'stock_number_5': [],
    'stock_number_6': [],
    'stock_number_7': [],
    'stock_number_8': [],
    'stock_number_9': [],
    'stock_number_10': []
}


# Class vehicle : intented to recognise cars, to read their properties
# and to change them with new attributes, typically when we change locations
# and statuses

class Car:
    def __init__(self):
        self.stock_number = "******"
        self.vin = "XXXXXXXXXXXXXXXXX"
        self.license_plate = "**-***-**"
        self.file = "BXX"
        self.zone = "ZONE_X"
        self.changelog = [""]

    def get_car_properties(self):
        print("récupération des propriétés du véh")
        return \
            "stock number : " + self.stock_number + "\n" + \
            "vin : " + self.vin + "\n" + \
            "licence plate : " + self.license_plate + "\n" + \
            "file : " + self.file + "\n" + \
            "zone : " + self.zone + "\n" + \
            " ; ".join(self.changelog)

    def set_car_properties(self, stock_number, vin, license_plate, file, zone, changelog):
        print("attribution de nouvelles propriétés")
        self.stock_number = stock_number
        self.vin = vin
        self.license_plate = license_plate
        self.file = file
        self.zone = zone
        self.changelog = changelog


car = Car()
print(car.get_car_properties())

car.set_car_properties("SN123456", "XXXXXXXX", "12_DFG_566", "B1", "Z_Stockage", ["F"])
print(car.get_car_properties())

print(car.__dict__)

# Definition of class File which refers to 'rangée' in French
# a file usually belongs to a zone, therefore we add it in attributes


class File:
    def __init__(self):
        self.file_name = "B0"
        self.capacity = 5
        self.occupied = 0
        self.zone_name = "Z0"

    def free_places(self):
        return self.capacity - self.occupied

    def get_file_properties(self):
        print("localisation du véh dans le parc")
        return "nom rangee: " + self.file_name + "\n" + \
               "places vides : " + self.free_places() + "/" + self.capacity

    def decrement_file(self):
        self.occupied = self.occupied + 1
        return self


file_example = File()
print(file_example.__dict__)

file_new = file_example.decrement_file()
print(file_new.__dict__)

