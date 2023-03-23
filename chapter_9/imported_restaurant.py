from restaurant import Restaurant

restaurant = Restaurant("Habibs", "arabian")
restaurant.describe_restaurant()

print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} clients.")

restaurant.set_number_served(13)

print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} clients.")

restaurant.increment_number_served(6)

print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} clients.")