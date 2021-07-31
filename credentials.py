import random
import string
import pyperclip
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
    
def generate_password(self,length):
    '''
    method for generating passwords for the accounts
    '''   
    letters = string.ascii_lowercase
    result_str = ' '.join(random.choice(letters) for i in range(length))
    print("Random string of  length", length, "is:", result_str)
generate_password(8)

@classmethod     
def search_credential(cls, account):
    '''
    method that returns credentials for an account
    '''   
    for credential in cls.credentials_list:
        if credential.account == account:
         return Credential 
     
@classmethod
def copy_password(cls, account):
    exist_credentials = Credential.search_credential(account)
    pyperclip.copy(exist_credentials.password)     
    
        