from user import User

class Admin(User):

    def __init__(self, first_name, last_name, age, genre, city, privileges):
        super().__init__(first_name, last_name, age, genre, city)
        self.privileges = privileges

    def show_privileges(self):
        print(f"The privileges of the user {self.first_name} are:")
        for privilege in self.privileges:
            print(privilege)

""" paulo = Admin("Paulo Renato", "Baliza Silva", 31, "male", "Goiania",
            ["can add post", "can delete post", "can ban user"])

paulo.show_privileges() """
