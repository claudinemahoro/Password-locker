class Credential:
	'''
	Class to help saving user's different accounts'credentials or  create  new ones.
	'''

	list_of_credentials =[]
	user_credentials_list = []

  def __init__(self,username,platform_name,account_name,password):
		'''
		Method to define the properties for each user's acounts object.
		'''

		self.username = username
		self.platform_name = platform_name
		self.account_name = account_name
		self.password = password

  @classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the first-name and password entered by the user already exist in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

  def save_credentials(self):
		'''
		Function to save the user's entered credentials
		'''

		Credential.list_of_credentials.append(self)