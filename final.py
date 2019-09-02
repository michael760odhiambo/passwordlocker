def create_details(fname,lname,account,password):
    '''
    Function to create a new Details
    '''
    new_details = Details(fname,lname,account,password)
    return new_details

def save_details(details):
    '''
    Function to save details
    '''
    details.save_details()

def del_details(details):
    '''
    Function to delete a details
    '''
    details.delete_details() 

def find_details(account):
    '''
    Function that finds a details by account and returns the details
    '''
    return Details.find_by_account(account)

def check_existing_details(account):
    '''
    Function that check if a details exists with that account and return a Boolean
    '''
    return Details.details_exist(account)

def display_details():
    '''
    Function that returns all the saved details
    '''
    return Details.display_details()

def main():

    print("Hello Welcome to your details list. What is your name?")
    user_name = input() 
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
         print("Use these short codes : cc - create a account, dc - display details, fc -find a details, ex -exit the details list ")

         short_code = input().lower()
         if short_code == 'cc':


             print("New Details")
             print("-"*10)

             print ("First name ....")
             f_name = input()

             print("Last name ...")
             l_name = input()

             print("account ...")
             account = input()

             print("password ...")
             password = input()


             save_details(create_details(f_name,l_name,account,password)) # create and save new details.
             print ('\n')
             print(f"New Details {f_name} {l_name} created")
             print ('\n') 

         elif short_code == 'dc':
             if display_details():
                 print("Here is a list of all your details")
                 print('\n')

                 for details in display_details():
                            print(f"{details.first_name} {details.last_name} .....{details.account}")

                            print('\n')
             else:
                                    print('\n')
                                    print("You dont seem to have any details saved yet")
         
         elif short_code == 'fc':
                           print('\n')
                           print("Enter the account you want to search for")

                           search_account = input()

                           if check_existing_details(search_account):

                               search_details = find_details(search_account)
                               print(f"{search_details.first_name} {search_details.last_name}")
                               print('-' * 20)

                               print(f"account.......{search_details.account}")
                               print(f"password.......{search_details.password}")

                           else:
                                 print("That details does not exist")

         elif short_code == "ex":
              print("Bye .......")
              break
                           
         else:
                            print("I really didn't get that. Please use the short codes")                        
                           
              