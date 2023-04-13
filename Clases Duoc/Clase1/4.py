# create a system that allows to validate the user and password from a worker, the only two users are pedro and angel, and their passwords are 1234 and a4s1

def validate_user(user, password):
    if user == "pedro" and password == "1234":
        return True
    elif user == "angel" and password == "a4s1":
        return True
    else:
        return False