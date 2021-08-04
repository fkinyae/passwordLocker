def generate_password(self,length):
    '''
    method for generating passwords for the accounts
    '''   
    letters = string.ascii_lowercase
    result_str = ' '.join(random.choice(letters) for i in range(length))
    print("Random string of  length", length, "is:", result_str)
generate_password(8,6)




    def gen_password():
        print('Hello, generate your password here!')
        
        length = int(input('\nEnter the password length:'))
        
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        
        all = lower + upper + num + symbols
        
        temp = random.sample(all, length)
        
        password = "".join(temp)
        
        print(password)