class User:
	'''
	Class to create user account for this app and save the details
	'''


	def __init__(self,first_name,last_name,password):


		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	users_list = []

