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

    def increment_file(self):
        self.occupied = self.occupied - 1

######################################################################################################################


def initialize_files(vp):
    x = dict()
    for elem in vp:
        x[elem] = File()
        x[elem].file_name = elem
    return x


def list_to_car(liste):
    return Car(liste[0], liste[1], liste[2], liste[3], liste[4], liste[5])


def car_to_list(ca: Car):
    return [ca.stock_number, ca.vin, ca.license_plate, ca.file, ca.status, ca.changelog]


def import_expected_cars_today(t, d0):
    for x in t:
        if x[0] in d0:
            pass
        else:
            d0[x[0]] = [x[0], x[1], x[2]]
    return d0


def check_car(sn, dic):
    # a function to check whether the car is expected to enter in LC
    # dic is the list of cars located in LC
    # the so-called list is stored in the table table_cars_at_lc
    if sn in dic:
        return "car accepted because it belongs to expected cars"
    else:
        return "car not expected"


valid_placements = ['F50', 'F49', 'F48', 'F47', 'F46', 'F45', 'F44', 'F43', 'F42', 'F41', 'F40', 'F39', 'F38', 'F37', 'F36', 'F35','F34','F33','F32','F31','F30','F29','F28','F27','F26','F25','F24','F23','F22','F21','F20','F19','F18','F17','F16','F15','F14','F13','F12','F11','F10','F9','F8','F7','F6','F5','F4','F3','F2','F1']
table_files = {}
table_files = initialize_files(valid_placements)

table_cars_at_lc = {}
table_cars_expected = {'X4': ['X4', 'V4', 'L4'], 'X1': ['X1', 'V1', 'L1']}
table_cars_left_lc = {}


def add_car_to_lc(ca: Car):
    # the test check car in LC is supposed to be negative at this point
    if ca.stock_number in table_cars_at_lc:
        pass
    else:
        ca.changelog.append("car was admitted to LC")
        ca.status = 1
        table_cars_at_lc[ca.stock_number] = car_to_list(ca)


def assign_car_placement(c: Car, placement):
    if placement in valid_placements:
        if table_files[placement].occupied < 5:
            c.file = placement
            c.status = 2
            c.changelog.append("car " + c.stock_number + " was moved to file " + placement + " at time " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            table_files[placement].decrement_file()
            table_files[placement].list_cars.append(car_to_list(c))
        else:
            return "not possible to add the car in file"
    else:
        return "not possible"


def car_ready_to_leave_lc(c: Car):
    my_file = c.file
    table_files[my_file].increment_file()
    table_files[my_file].list_cars.remove(car_to_list(c))
    c.status = 3
    c.file = "leaving zone"
    c.changelog.append("car " + c.stock_number + " ready to leave the LC at time ")
    table_cars_at_lc.pop(c.stock_number)


car1 = Car()
print(car1.__dict__)
car1.set_car_properties("X1", "v", "l", "", 0, [])
print(car1.__dict__)
print(table_cars_expected)
print(check_car(car1.stock_number, table_cars_expected))
add_car_to_lc(car1)
print(car1.__dict__)
print(table_cars_at_lc)
print(table_files)
assign_car_placement(car1, "F2")
print(car1.__dict__)
print(table_cars_at_lc)
print(table_files['F2'].__dict__)
# car_ready_to_leave_lc(car1)
print(car1.__dict__)
print(table_cars_at_lc)
print(table_files['F2'].__dict__)


def display_table_cars_at_lc():
    for elem in table_files:
        print(table_files[elem].__dict__)

display_table_cars_at_lc()
