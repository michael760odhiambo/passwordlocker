import pyperclip
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Details(Person):
  details_list = []
  def __init__(self, fname, lname, account,password):
    super().__init__(fname, lname)
    self.account = account
    self.password = password
   

  def welcome(self):
      print('your first name:')
      fname = input()
      print('your last name:')
      lname = input()
      
    
      print("Welcome", fname, lname, "to", self.account, self.password)
      input('create a password: ')
  
  def save_details(self):
    '''
    save_details method saves details objects into details_list
    '''
    Details.details_list.append(self)

  def delete_details(self):

    '''
    delete_details method deletes a saved details from the details_list
    '''

    Details.details_list.remove(self)       

  @classmethod
  def find_by_account(cls,account):
    '''
    Method that takes in a account and returns a details that matches that account.

    Args:

    account: account to search for
    Returns :
    Details of person that matches the account.
    '''

    for details in cls.details_list:
      if details.account == account:
                return details

  @classmethod
  def details_exist(cls,account):
    '''
    Method that checks if a details exists from the details list.
    Args:
    account: account to search if it exists
    Returns :
    Boolean: True or false depending if the details exists
    '''
    for details in cls.details_list:
       if details.account == account:
                    return True
    return False


           
  @classmethod
  def display_details(cls):
    '''
    method that returns the contact list
    '''
    return cls.details_list   
            
     
  

x = Details("", "", ' passwordlocker','password')
x.welcome()
print('do you have an account: ')
input('enter your password: ')

  

        

    
    
   

   

     





