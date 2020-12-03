import datetime

# Class vehicle : intented to recognise cars, to read their properties
# and to change them with new attributes, typically when we change locations
# and statuses

class Car:
    def __init__(self):
        self.stock_number = "******"
        self.vin = "XXXXXXXXXXXXXXXXX"
        self.license_plate = "**-***-**"
        self.file = "BXX"
        self.status = 0
        self.changelog = [""]

    def get_car_properties(self):
        print("récupération des propriétés du véh")
        return \
            "stock number : " + self.stock_number + "\n" + \
            "vin : " + self.vin + "\n" + \
            "licence plate : " + self.license_plate + "\n" + \
            "file : " + self.file + "\n" + \
            " ; ".join(self.changelog)

    def set_placement(self, place):
        self.file = place
        self.status = 2

    def display_changelog(self):
        print(self.changelog)

    def set_car_properties(self, stock_number, vin, license_plate, file, zone, changelog):
        print("attribution de nouvelles propriétés")
        self.stock_number = stock_number
        self.vin = vin
        self.license_plate = license_plate
        self.file = file
        self.changelog = changelog


car = Car()
print(car.get_car_properties())

All_Cars = {
    'X1': ["X1", "V1", "L1", "E1"],
    'X2': ["X2", "V2", "L2", "E2"],
    'X3': ["X3", "V3", "L3", "E3"]
}

# tomorrow

#csv = [["X4", "V4", "L4", "E4"], ["X5", "V5", "L5", "E5"], ["X1", "V1", "L1", "E1"]]

#for elem in csv:
#    if elem[0] exists in All_cars:
#    else:
#        All_Cars.append(elem)


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

    def free_places(self):
        return self.capacity - self.occupied

    def get_file_properties(self):
        print("localisation du véh dans le parc")
        return "nom rangee: " + self.file_name + "\n" + \
               "places vides : " + self.free_places() + "/" + self.capacity

    def decrement_file(self):
        self.occupied = self.occupied + 1
        return self


class Operator:
    def __init__(self):
        self.firstname = ""
        self.surname = ""
        self.email = ""
        self.role = ""

    def set_operator_attributes(self, firstname, surname, email, role):
        print("the operator is")
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.role = role


operator1 = Operator()
operator1.set_operator_attributes("john", "wellington", "john.wellignton@auto1.com", "responsible of dispatch")

file_example = File()
print(file_example.__dict__)

file_new = file_example.decrement_file()
print(file_new.__dict__)

# Simulation: a car enters to the LC, what happens next
# Set car properties by reading the RD : planned cars in LC

# import pandas

# a new car enters



car = Car()
print(car.__dict__)

# input function : the operator can enrich the new object with attributes


#let's say we have files empty
F1 = File(); F1.file_name = "F1"
F2 = File(); F2.file_name = "F2"
F3 = File()
F4 = File()
F5 = File()
F6 = File()
F7 = File()
F8 = File()
F9 = File()
F10 = File()

car1 = Car()

car1.vin = "CDDKJHZKJEDHZ"
car1.stock_number = "CC7812Z1"

F1.decrement_file()
car1.file = "F1"

print(car1.__dict__)
print(F1.__dict__)

car3 = Car()
car3.stock_number = input("hey please enter stock number")
car3.vin = input("hey please enter vin")
car3.file = input("hey please choose a valid free place in the file")

# since a place wan assignde to the car, i need to modify the file
F1.decrement_file()

car3.changelog.append(car3.stock_number + " was moved to " + F1.file_name + " at time" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + operator1.firstname + " " + operator1.surname)

print(car3.__dict__)
print(F1.__dict__)
print(operator1.__dict__)
car3.display_changelog()
