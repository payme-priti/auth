from django.test import TestCase
from api.models import User

class UserModelTestCase(TestCase):
    def test_user_creation(self):
        # Create a user
        user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

        # Check if the user is saved correctly
        self.assertEqual(User.objects.count(), 1)
        saved_user = User.objects.first()
        self.assertEqual(saved_user.username, 'testuser')
        self.assertEqual(saved_user.email, 'testuser@example.com')
        self.assertEqual(saved_user.password, 'testpass')

    def test_unique_fields(self):
        # Create a user with the same username and email
        User.objects.create(
            username='existinguser',
            email='existing@example.com',
            password='existingpass'
        )

        # Try to create a new user with the same username
        with self.assertRaises(Exception) as context:
            User.objects.create(
                username='existinguser',
                email='new@example.com',
                password='newpass'
            )
        self.assertIn('unique', str(context.exception))

        # Try to create a new user with the same email
        with self.assertRaises(Exception) as context:
            User.objects.create(
                username='newuser',
                email='existing@example.com',
                password='newpass'
            )
            self.assertIn('An error occurred in the current transaction.', str(context.exception))
        
