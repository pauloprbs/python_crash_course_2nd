class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name.title()}.")
        print(f"It is a {self.cuisine_type} restaurant.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors[:]

    def display_flavors(self):
        print("We serve this flavors of ice cream:")
        for flavor in self.flavors:
            print(flavor)

mcdonalds = IceCreamStand("McDonalds", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])

mcdonalds.display_flavors()
