class Users():
    user_id=1

    def __init__(self,user_name,email,password,status):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.user_id = Users.user_id
        self.user_id +=1


class User(Users):

    def __init__(self,user_name,email,password,status):
        Users.__init__(self,user_name,email,password,status)
        self.status = 'normal'

class Moderators(Users):

    def __init__(self,user_name,email,password,status):
        Users.__init__(self,user_name,email,password,status)
        self.status = 'moderator'

class Admin(Users):

    def __init__(self,user_name,email,password,status):
        Users.__init__(self,user_name,email,password,status)
        self.status = 'admin'

