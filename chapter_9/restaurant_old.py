class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name.title()}.")
        print(f"It is a {self.cuisine_type} restaurant.")

first_restaurant = Restaurant("Bologna", "italian")
first_restaurant.describe_restaurant()

second_restaurant = Restaurant("Habibs", "arabian")
second_restaurant.describe_restaurant()

third_restaurant = Restaurant("Nativas", "brazilian")
third_restaurant.describe_restaurant()
