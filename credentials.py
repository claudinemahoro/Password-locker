import random 
import string 
from user import User  

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

  @classmethod
	def delete_credentials(self):
		'''
		Function to help deleting the saved credentials if needed
		'''

		Credential.list_of_credentials.remove(self)

  def generate_password(size=8, char=string.ascii_lowercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate a password for a user if needed.
		'''
		password_gen=''.join(random.choice(char) for _ in range(size))
		return password_gen

  @classmethod
	def display_credentials(cls,username):
		'''
		Method to display the user's credentials saved.
		'''
		user_credentials_list = []
		for credential in cls.list_of_credentials:
			if credential.username == username:
				user_credentials_list.append(credential)
		return user_credentials_list

  @classmethod
	def find_by_credential_name(cls, platform_name):
		'''
		Method that takes in a platform_name and returns a credentials that matches that platform_name.
		'''
		for credential in cls.list_of_credentials:
			if credential.platform_name == platform_name:
				return credential
		return False

    