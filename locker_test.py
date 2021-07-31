import unittest
from locker import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviour
    '''
    def setUp(self):
        '''
        setup method to run before each test cases.
        '''
        self.new_user = User("Francis","khyegsbh") #user object created
        
        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly 
            '''
            self.assertEqual(self.new_user.username,'Francis')
            self.assertEqual(self.new_user.password,'khyegsbh')
            
        def test_save_user(self):
            '''
            test_save_user test case to test if the user is saved on the user_list
            '''
            self.new_user.save_user() #save the user
            self.assertEqual(len(User.user_list),1)
            
    if __name__ == '_main_':
        unittest.main()        

            