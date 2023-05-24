class resturant:
    '''create a resturant'''
    def __init__(self, resturant_name, cuision_type):
        self.resturant_name = resturant_name
        self.cuision_type = cuision_type
        self.number_served = 0

    def describe_resturant(self):
        description = f"The name of the resturant_name is {self.resturant_name}, and its cuision type is {self.cuision_type}, today has {self.number_served} customers"
        return description

    def open_resturant():
        print("It's opening")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increase):
        self.number_served += increase