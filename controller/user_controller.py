accounts = []
# App user options
user_options = ('------User options------\n1. Sign up\n2. Login\n3. Exit application')
def add_account(username, email, account_type, password):
    if username != "" or email != "" or  account_type != "" or password != "":
        user = {}
        user['username'] = username
        user['email'] = email
        user['account_type'] = account_type
        user['password'] = password
        accounts.append(user)
    return False

def login(email, password):
  for user in accounts:
    if user['email'] == email and user['password'] == password:
      return True
  return False

def select_user_method(option):
    option = int(option)
    if option == 1:
        username = input("enter username: ")
        email = input("enter email: ")
        account_type = input("enter account type: ")
        password = input("enter password: ")
        if add_account(username, email, account_type, password):
            print("{} signed up successfully".format(email))
            return True
        return False	
    else:		
        email = input("enter email: ")
        password = input("enter password: ")
        if login(email, password):
            return "{} is now logged in".format(email)
        return False
