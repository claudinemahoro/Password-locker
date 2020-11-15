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