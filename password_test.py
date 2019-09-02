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
        self.new_details = Details("","","","") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_details.firstname,"")
        self.assertEqual(self.new_details.lastname,"")
        self.assertEqual(self.new_details.account,"")
        self.assertEqual(self.new_details.password,"")

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
        test_details = Details("","","","") # new detail
        test_details.save_details()
        self.assertEqual(len(Details.details_list), 2)

    def test_delete_details(self):
            '''
            test_delete_details to test if we can remove a contact from our details list
            '''
            self.new_details.save_details()
            test_details = Details("","","","") # new detail
            test_details.save_details()

            self.new_details.delete_details()# Deleting a detail object
            self.assertEqual(len(Details.details_list),1)  

    def test_find_details_by_account(self):
        '''
        test to check if we can find a details by account and display information
        '''

        self.new_details.save_details()
        test_details = Details("","","","") # new details
        test_details.save_details()

        found_details = Details.find_by_account("")

        self.assertEqual(found_details.password,test_details.password)

    def test_details_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the details.
        '''

        self.new_details.save_details()
        test_details = Details("","","","") # new details
        test_details.save_details()

        details_exists = Details.details_exist("")

        self.assertTrue(details_exists) 

    def test_display_all_details(self):
        '''
        method that returns a list of all detals saved
        '''

        self.assertEqual(Details.display_details(),Details.details_list)         

if __name__ == '__main__':
    unittest.main()