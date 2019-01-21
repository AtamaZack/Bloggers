def login(self,email, password, accounts):
    email = input("Please enter your email:\n")
    password = input("Please enter your password:\n")

    for user in accounts:
        if user["email"] == email and password["password"] == password:
            if user["status"] == "normal_user":
                print("user successfully logged in!")
            if user["status"] == "moderate_user":
                print("user successfully logged in!")
            else:
                print("Admin successfully logged in!")
        else:
            print("invalid login credentials")
login(users_list)
