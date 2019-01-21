def login(email, password):
  for user in accounts:
    if user['email'] == email and user['password'] == password:
      return True
  return False
