class UserException(Exception):
    def __init__(self):
        self.demo = "you created a User defined exception"
try:
    print("Demo for user defined exception \n")
    raise UserException
except UserException:
    print(UserException().demo)
