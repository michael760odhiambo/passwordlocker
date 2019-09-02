import unittest
from password import Details

class TestPerson(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Details.details_list = []


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_details = Details("James","Muriuki","#james","james@ms.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_details.firstname,"James")
        self.assertEqual(self.new_details.lastname,"Muriuki")
        self.assertEqual(self.new_details.account,"#james")
        self.assertEqual(self.new_details.password,"james@ms.com")

    def test_save_details(self):
        '''
        test_save_details test case to test if the contact object is saved into
         the contact list
        '''
        self.new_details.save_details() # saving the new detail
        self.assertEqual(len(Details.details_list),1)

    def test_save_multiple_details(self):
        '''
        test_save_multiple_details to check if we can save multiple contact
        objects to our contact_list
        '''

          
        self.new_details.save_details()
        test_details = Details("Test","user","#james","test@user.com") # new detail
        test_details.save_details()
        self.assertEqual(len(Details.details_list), 2)

    def test_delete_details(self):
            '''
            test_delete_details to test if we can remove a contact from our details list
            '''
            self.new_details.save_details()
            test_details = Details("Test","user","#james","test@user.com") # new detail
            test_details.save_details()

            self.new_details.delete_details()# Deleting a detail object
            self.assertEqual(len(Details.details_list),1)  

    def test_find_details_by_account(self):
        '''
        test to check if we can find a details by account and display information
        '''

        self.new_details.save_details()
        test_details = Details("Test","user","#james","test@user.com") # new details
        test_details.save_details()

        found_details = Details.find_by_account("#james")

        self.assertEqual(found_details.password,test_details.password)
          

if __name__ == '__main__':
    unittest.main()