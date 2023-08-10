#!/usr/bin/python3
"""Defines unittests for"user.py"""

import os
import unittest
import models
from models.user import User

class test_user():

    def test_fields_not_empty(self):

        """Test if fields are not  empty."""
        user = User()
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.password)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)

    def test_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_email_is_public_str(self):
        """unittest for email validation"""

        user = User(email='test@example.com', public=True)
     
        self.assertEqual(str(user), 'User(email=test@example.com, public=True)')

    def test_id_is_public_str(self):
        """check id for validation"""

        self.assertEqual(str, type(User().id))

    def test_email_is_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_str(self):
        self.assertEqual(str, type(User.last_name))


if __name__ == '__main__':
    unittest.main()
