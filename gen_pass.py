def generate_password(self,length):
    '''
    method for generating passwords for the accounts
    '''   
    letters = string.ascii_lowercase
    result_str = ' '.join(random.choice(letters) for i in range(length))
    print("Random string of  length", length, "is:", result_str)
generate_password(8,6)