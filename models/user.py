class Users():
    user_id=1

    def __init__(self,first_name,last_name,email,password,status):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user_id = Users.user_id
        self.user_id +=1


class User(Users):

    def __init__(self,first_name,last_name,email,password,status):
    Users.__init__(self,first_name,last_name,email,password,status):
        self.status = 'user'

class Moderators(Users):

    def __init__(self,first_name,last_name,email,password,status):
    Users.__init__(self,first_name,last_name,email,password,status):
        self.status = 'moderator'

class Admin(Users):

    def __init__(self,first_name,last_name,email,password,status):
    Users.__init__(self,first_name,last_name,email,password,status):
        self.status = 'admin'