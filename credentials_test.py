
import unittest
from user import User  
from credentials import Credential 

class TestUser(unittest.TestCase):

    '''
    Test class that defines the test cases for the the user class behaviours.

    '''
    
     def setUp(self):
        '''
        Setup method to run before each test case 
        ''' 
        self.new_user = User('Claudine', 'Mahoro', '2580)
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Claudine")
        self.assertEqual(self.new_user.last_name,"Mahoro")
        self.assertEqual(self.new_user.password,"2580")
       
    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the users list
		'''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
    def cleanUp(self):
       '''
        cleanUp method that does clean up after each test case has run.
       '''
        User.users_list = []

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for the the credential class behaviours.

   '''
    def setUp(self):
        '''
		Setup method to run before each test case
		'''
        self.new_credential = Credential('evelyne','instagram','evelyne250','123456')

    

if __name__ == '__main__':
    unittest.main()
