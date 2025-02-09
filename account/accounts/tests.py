from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase
from rest_framework import status
from account.accounts.models import Waiter

class WaiterAuthTests(APITestCase):
    """Test cases for Waiter login and logout."""

    def setUp(self):
        """Set up test data."""
        self.waiter = Waiter.objects.create(
            username="testwaiter",
            password=make_password("Test@1234")  # Hash the password
        )
        self.login_url = "/accounts/login/"
        self.logout_url = "/accounts/logout/"

    def test_waiter_login_success(self):
        """Test successful login."""
        data = {"username": "testwaiter", "password": "Test@1234"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Login successful")

    def test_waiter_login_fail_invalid_password(self):
        """Test login with incorrect password."""
        data = {"username": "testwaiter", "password": "WrongPass"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Invalid credentials")

    def test_waiter_logout(self):
        """Test logout after login."""
        login_data = {"username": "testwaiter", "password": "Test@1234"}
        self.client.post(self.login_url, login_data)  # Log in first
        response = self.client.post(self.logout_url)  # Then log out
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Logout successful")
