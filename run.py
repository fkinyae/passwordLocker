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
      authenticate_user = 