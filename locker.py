class User:
    '''
    Class that generates new instances of users
    '''
    user_list = [] #list of users.add
    
    def __init__(self, username, password ):
        '''
        defining the properties of a user
        '''
        self.username = username
        self.password = password
        
        #save a user
    def save_user(self):
        '''
        method that saves a new instance of a user into the list
        '''
        User.user_list.append(self)
        
    @classmethod
    def display_users(cls):
        '''
        method that returns the users list
        '''
        return cls.user_list
        