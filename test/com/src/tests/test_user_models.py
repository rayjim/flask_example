'''
Created on Nov 26, 2017

@author: ray
'''
import unittest
from app.models import User

class TestModelTestCase(unittest.TestCase):


    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)
        
    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password
    
    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('cad'))
        
    def test_password_salts_are_random(self):
        u = User(password='cat')
        u1 = User(password='cat')
        self.assertTrue(u.password_hash != u1.password_hash)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()