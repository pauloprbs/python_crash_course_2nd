class Car:

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer += miles

class Battery:

    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def descriptive_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 350

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
        else:
            print("This car already have a 100KWh battery.")

class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.descriptive_name())
my_tesla.battery.descriptive_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.descriptive_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
