import unittest
from user import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for the behaviour of the user class
    '''
    
    def setUp(self):
            '''
            set up method to run before each test cases
            '''
            self.new_user = User("francis", "klmnopqrst")
            
    def tearDown(self):
        '''
        cleans up after each testcase has run
        '''
        User.users_list = []       
            
    def test_init(self):
            '''
            test init test case to test if the object is initialized properly
            '''    
            self.assertEqual(self.new_user.username,"francis")
            self.assertEqual(self.new_user.password,"klmnopqrst")
            
    def test_save_user(self):
            '''
             test if the user object is saved in the user list
            '''    
            self.new_user.save_user()
            self.assertEqual(len(User.users_list),1)
            
    def test_delete_user(self):
        '''
        test to check whether we can remove a user from our users list
        '''        
        self.new_user.save_user()
        test_user = User("francis", "klmnopqrst")
        test_user.save_user()
        
        self.new_user.delete_user()
        
        self.assertEqual(len(User.users_list),1)
    
    
if __name__ == '__main__':
    unittest.main()    