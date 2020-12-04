import datetime


# Class vehicle : intented to recognise cars, to read their properties
# and to change them with new attributes, typically when we change locations
# and statuses

#####################################################################################################################

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


class Car:
    def __init__(self):
        self.stock_number = ""
        self.vin = ""
        self.license_plate = ""
        self.file = ""
        self.status = 0
        self.changelog = [""]

    def car_to_list(self):
        print(self.stock_number, self.vin, self.license_plate, self.file, self.status, self.changelog)

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

    def set_car_properties(self, stock_number, vin, license_plate, file, status, changelog):
        self.stock_number = stock_number
        self.vin = vin
        self.license_plate = license_plate
        self.file = file
        self.status = status
        self.changelog = changelog


class File:
    def __init__(self):
        self.file_name = ""
        self.capacity = 5
        self.occupied = 0
        self.list_cars = []

    def free_places(self):
        return self.capacity - self.occupied

    def decrement_file(self):
        self.occupied = self.occupied + 1

######################################################################################################################


def list_to_car(liste):
    return Car(liste[0], liste[1], liste[2], liste[3], liste[4], liste[5])

table_cars_expected_0 = {'X4': ['X4', 'V4', 'L4'],
                         'X1': ['X1', 'V1', 'L1']}

# the log team sends a scv with expected cars we need to import
# headers are : stock_number, vin, licence_plate
# UI : we need to create a button : upload csv expected cars EC
EC = [['X1', 'V1', 'L1'], ['X2', 'V2', 'L2'], ['X3', 'V3', 'L3']]


def import_expected_cars_today(t, d0):
    for x in t:
        if x[0] in d0:
            pass
        else:
            d0[x[0]] = [x[0], x[1], x[2]]
    return d0


table_cars_expected_0 = import_expected_cars_today(EC, table_cars_expected_0)
print('##############################################')
print(EC)
print(table_cars_expected_0)
print('##############################################')


######################################################################################################################


def check_car(c, dic):
    # a function to check whether the car is expected to enter in LC
    # dic is the list of cars located in LC
    # the so-called list is stored in the table table_cars_at_lc_0
    if c[0] in dic:
        return "car accepted because it belonfs to expected cars"
    else:
        return "car not expected"

car_test_entrance = ['X5', 'V1', 'L1']
print(check_car(car_test_entrance, table_cars_expected_0))
print('test check car #######################""')


valid_placements_0 = ['F50', 'F49', 'F48', 'F47', 'F46', 'F45', 'F44', 'F43', 'F42', 'F41', 'F40', 'F39', 'F38', 'F37', 'F36', 'F35','F34','F33','F32','F31','F30','F29','F28','F27','F26','F25','F24','F23','F22','F21','F20','F19','F18','F17','F16','F15','F14','F13','F12','F11','F10','F9','F8','F7','F6','F5','F4','F3','F2','F1']
table_cars_at_lc_0 = {}
table_cars_expected_0 = {}
table_cars_left_lc_0 = {}
table_files_0 = {}


def initialize_files():
    for elem in valid_placements_0:
        table_files_0[elem] = File()
        table_files_0[elem].file_name = elem


initialize_files()


def add_car_to_lc(ca: Car, table_cars_at_lc):
    # the test check car in LC is supposed to be negative at this point
    if ca.stock_number in table_cars_at_lc_0:
        pass
    else:
        ca.changelog.append("car was admitted to LC")
        my_list = (ca.stock_number, ca.vin, ca.license_plate, "", 0, ["car was admitted to LC"])
        table_cars_at_lc[ca.stock_number] = my_list

car = Car()
car.set_car_properties('X1', 'V1', 'L1', "", 0, [])

add_car_to_lc(car, table_cars_at_lc_0)
print(table_cars_at_lc_0)
print("???????????????????????????????adding a car to lc")
print(car.get_car_properties())


def assign_car_placement(c: Car, placement):
    if placement in valid_placements_0:
        c.file = placement
        c.status = 2
        c.changelog.append("car " + c.stock_number + " was moved to file " + placement + " at time " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        table_files_0[placement].decrement_file()


assign_car_placement(car, "F10")
print(car.__dict__)
print(table_files_0['F10'].__dict__)
print(table_files_0['F11'].__dict__)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")



All_Cars = {
    'X1': ["X1", "V1", "L1", "E1"],
    'X2': ["X2", "V2", "L2", "E2"],
    'X3': ["X3", "V3", "L3", "E3"]
}

# tomorrow

# csv = [["X4", "V4", "L4", "E4"], ["X5", "V5", "L5", "E5"], ["X1", "V1", "L1", "E1"]]

# for elem in csv:
#    if elem[0] exists in All_cars:
#    else:
#        All_Cars.append(elem)


car.set_car_properties("SN123456", "XXXXXXXX", "12_DFG_566", "B1", 0, ["F"])
print(car.get_car_properties())

print(car.__dict__)


# Definition of class File which refers to 'rangée' in French
# a file usually belongs to a zone, therefore we add it in attributes

operator1 = Operator()
operator1.set_operator_attributes("john", "wellington", "john.wellignton@auto1.com", "responsible of dispatch")

file_example = File()
print(file_example.__dict__)

file_example.decrement_file()
print(file_example.__dict__)

# Simulation: a car enters to the LC, what happens next
# Set car properties by reading the RD : planned cars in LC

# import pandas

# a new car enters


car = Car()
print(car.__dict__)

# input function : the operator can enrich the new object with attributes


# let's say we have files empty
F1 = File()
F2 = File()
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

car3.changelog.append(
    car3.stock_number + " was moved to " + F1.file_name + " at time" + datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S") + " " + operator1.firstname + " " + operator1.surname)

print(car3.__dict__)
print(F1.__dict__)
print(operator1.__dict__)
car3.display_changelog()
