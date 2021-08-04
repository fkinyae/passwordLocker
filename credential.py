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
            if (user.username == username and user.password == password ):
                firstuser == user.username
        return firstuser
    
    def __init__(self, account, userName, passWord):
        '''
        method that initializes the credentials to be stored
        '''   
        self.account = account
        self.userName = userName    
        self.passWord = passWord 
        
    def save_credential(self):
        '''
        method to save credentials
        '''    
        Credential.credentials_list.append(self)
        
    def delete_credential(self):  
        '''
        method for deleting a credential from the list
        ''' 
        Credential.credentials_list.remove(self)
        
    @classmethod  
    def find_by_account(cls, account):
        '''
        method to search credentials by account
        ''' 
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
        
            