elif short_code == "dc":
                                if display_my_credentials():
                                    print("Here is a list of your accounts: ")
                            
                                    print('*' * 30)
                                   print('_'* 30)
                          for account in display_accounts_details():
                               print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                               print('_'* 30)
                        print('*' * 30)