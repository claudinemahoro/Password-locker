
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
       
if __name__ == '__main__':
    unittest.main()
