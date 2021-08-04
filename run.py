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
    
def find_a_credential():    