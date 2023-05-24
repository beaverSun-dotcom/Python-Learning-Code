
class User:
    '''some information about a user'''
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = login_attempts
    def describe_user(self):
        print(f"The name of the user is {self.first_name} {self.last_name}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attemps += 1

    def reset_login_attempts(self):
        self.login_attemps = 0

        
class Privileges:
    def __init__(self):
        self.privileges = ['can delete post', 'can add post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"Admin can {privilege}")


class Admin(User):
    '''A special user'''
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges()