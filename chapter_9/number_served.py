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

restaurant = Restaurant("Habibs", "arabian")
restaurant.describe_restaurant()

print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} clients.")

restaurant.set_number_served(13)

print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} clients.")

restaurant.increment_number_served(6)

print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} clients.")
