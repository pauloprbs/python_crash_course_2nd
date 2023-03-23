class User:

    def __init__(self, first_name, last_name, age, genre, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.genre = genre
        self.city = city

    def describe_user(self):
        print(f"name: {self.first_name.title()} {self.last_name.title()}.")
        print(f"age: {self.age}.")
        print(f"genre: {self.genre}.")
        print(f"city: {self.city.title()}.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}.")

paulo = User("Paulo Renato", "Baliza Silva", 31, "male", "Goiania")
paulo.greet_user()
paulo.describe_user()

felicia = User("Felicia", "Baliza", 2, "female", "Goiania")
felicia.greet_user()
felicia.describe_user()
