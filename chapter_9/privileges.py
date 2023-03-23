class User:

    def __init__(self, first_name, last_name, age, genre, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.genre = genre
        self.city = city
        self.login_attemps = 0

    def describe_user(self):
        print(f"name: {self.first_name.title()} {self.last_name.title()}.")
        print(f"age: {self.age}.")
        print(f"genre: {self.genre}.")
        print(f"city: {self.city.title()}.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}.")

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0

class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"The privileges of the user are:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):

    def __init__(self, first_name, last_name, age, genre, city, privileges):
        super().__init__(first_name, last_name, age, genre, city)
        self.privileges = Privileges(privileges)

paulo = Admin("Paulo Renato", "Baliza Silva", 31, "male", "Goiania",
            ["can add post", "can delete post", "can ban user"])

paulo.privileges.show_privileges()
