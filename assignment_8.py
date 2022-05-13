
#vehicle is the base class

class Vehicle:

    def __init__(self):

        #dictionary of options

        self.vehicle_options = {'make': '', 'model': ''}
       

 

    def setMake(self, make):

        self.vehicle_options['make'] = make

 

    def setModel(self, model):

        self.vehicle_options['model'] = model

 

    def displayOptions(self):

        print("")

        print(f"You successfully created a vehicle and here are the options you entered.")

        print(f"The make: {self.vehicle_options['make']}")

        print(f"The model: {self.vehicle_options['model']}")

        print("")

 

#car inherits from vehicle

class Car(Vehicle):

    def __init__(self):

        super().__init__()

 

    #add the number of doors to the dictonary

    def setnumDoors(self, numDoors):

        self.vehicle_options['numDoors'] = numDoors

 

    #override the method in the vehicle class

    def displayOptions(self):

        print("")

        print(f"You successfully created a car and here are the options you entered.")

        print(f"The make: {self.vehicle_options['make']}")

        print(f"The model: {self.vehicle_options['model']}")

        print(f"The number of doors: {self.vehicle_options['numDoors']}")

        print("")

 

#pickup inherits from vehicle

class Pickup(Vehicle):

    def __init__(self):

        super().__init__()

 

    #add the bed length to the dictionary

    def setBedLength(self, bedLength):

        self.vehicle_options['bedLength'] = bedLength

 

    #override the method in the vehicle class

    def displayOptions(self):

        print("")

        print(f"You successfully created a pickup and here are the options you entered.")

        print(f"The make: {self.vehicle_options['make']}")

        print(f"The model: {self.vehicle_options['model']}")

        print(f"The bed length: {self.vehicle_options['bedLength']}")

        print("")


#### Module Level Functions ####
def run_program():
    user_input = input("Would you like to make a car or a pickup truck? ")
    if (user_input.lower() == 'car'): 
        #we make a car
        new_car = Car()
        new_car.vehicle_options['make'] = 'Honda'
        new_car.vehicle_options['model'] = 'Civic'
        new_car.setnumDoors(4)
        print(f'new car! new car dictionary is: {new_car.vehicle_options}')
        new_car.displayOptions()
    pass
run_program()
    

def run_program():
    user_input = input("What kind of truck would you like? ")   #type in pickup truck here.
    if (user_input.lower() == 'pickup truck'):
         #make pickup truck
        new_truck = Pickup()
        new_truck.vehicle_options['make'] = 'Ford'
        new_truck.vehicle_options['model'] = 'F150'
        new_truck.setBedLength(9)
        print(f'new pickup! new pickup directory is: {new_truck.vehicle_options}')
        new_truck.displayOptions()
    pass
run_program()





