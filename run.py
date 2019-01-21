from controller.user_controller import select_user_method
if __name__ == "__main__":
	# App user options
	user_options = ('------User options------\n1. Sign up\n2. Login\n3. Exit application')
	# comment operation options
	task_options = ('------comment funtion options------\n1. creating a comment\n2. View all comment\n3. deleting a comment')
	print(user_options)
	select_option = input("select an option: ")
	exit_status = False
	while exit_status == False:
		if select_option.isdigit() and int(select_option) <= 2:
			if select_user_method(select_option):
				print(task_options)
				break
			else:
				print({"error": "input field invalid"})
				print(user_options)
				select_option = input("select an option: ")
		elif select_option == str(3):
			exit_status = True
		else:		
			print("invalid input, try again")
			print(user_options)
			select_option = input("select an option: ")
	else:		
		print("Thanks for using the application")