 from locker import User
 
class Credential:
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
        
def save_credentials(self):
        '''
        method for storing new credentials
        '''   
        Credential.credentials_list.append(self)
        
def delete_credentials(self):
    '''
    method that deletes account credentials
    '''   
    Credential.credentials_list.remove(self)
     
    
        