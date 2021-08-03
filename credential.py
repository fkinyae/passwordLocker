from user import User

class Credential:
    '''
    the blueprint for creating new objects for credentials
    '''
    credentials_list = []
            
    def authenticate_user(cls, username, password):
        '''
        check whether the user is in our list
        '''  
        firstuser = ""   
        for user in User.users_list:
            