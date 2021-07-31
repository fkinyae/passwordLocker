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
    
    def delete_user(self):
        '''
        method deletes a saved user from the list
        '''
        User.user_list.remove(self)
        
        class Credentials:
            '''
            the blueprint for creating new objects for credentials
            '''
            credentials_list = []
            
    @classmethod
    def confirm_users(cls, username, password):
        '''
        method to confirm the user exists in the list
        '''
        current_user = ''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                current_user = user.username
                return current_user
            
    def __init__(self, account, username, password):
        '''
        method that defines the types of user credentials to be saved
        '''   
        self.account = account
        self.username = username
        self.password = password
        