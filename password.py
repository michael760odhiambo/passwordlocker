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
    save_details method saves contact objects into details_list
    '''
    Details.details_list.append(self)
    
        

        
     
  

x = Details("", "", ' passwordlocker','password')
x.welcome()
print('do you have an account: ')
input('enter your password: ')

  

        

    
    
   

   

     





