#Encapsulatiobn
class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def get_username(self):
        return self._username 
    
    def set_password(self, new_password):
        self.__password = new_password
        print("Password update successfully!")

    def login(self, username, password):
        return self._username == username and slf.__password == password
user = User(username="priya",password="123456")

username = input("Enter username:")
password = input("Enter password:")

if user.login(username,password):
    print("Welcome,{user.get_username()}!")
else:
    print("Invalid login details.")
    option = input("Do you want to reset your password?(yes/no):").lower()
if option == "yes":
    new_password = input("Enter your new password: ")
    user.set_password(new_password)
else:
    print("Goodbye")