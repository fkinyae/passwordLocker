#!/usr/bin/env python3.9
from credential import Credential
from user import User

def create_new_user(username, password):
    '''
    Function that creates a user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()
    
def del_user(user):
    '''
    Function that deletes a user
    '''  
    user.delete_user()
    
def user_login(username, password):
    '''
    check user authentication
    '''  
    authentic_user =  Credential.authenticate_user(username, password)
    return authentic_user

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()
    
def delete_credential(credential):
    '''
    Function to delete credential
    '''    
    credential.delete_credential()
    
def find_a_credential(account):  
      '''
      Function that searches for credentials
      '''
      return Credential.find_by_account(account)

def check_credential_existence(account):
    '''
    Function that checks the existence of a credential
    '''
    return Credential.find_credential(account)

def display_my_credentials():
    '''
    Function to display my credentials
    '''
    return Credential.display_credentials()

def generate_password():
    '''
    generates random passwords
    '''
    get_password = Credential.gen_password()
    return get_password

def main():
    print("Hi.. Welcome to Password Locker  your modern passwords store! What is your name? ")
    user_name = input()
    
    print(f"Hello { user_name } , What can I do for you today? ")
    print('\n')
    
    while True:
                    print("Use the following short codes to perform your operation: cc - create a new user account,  ")
    
if __name__ == '__main__':
    main()    