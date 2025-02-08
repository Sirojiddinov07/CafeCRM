from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from .models import Waiter



class WaiterService:

    def login_waiter(request, username, password):
        """Authenticates a waiter and creates a session login."""
        waiter = get_object_or_404(Waiter, username=username)

        if not check_password(password, waiter.password):
            raise ValueError("Invalid credentials")

        login(request, waiter)  # Logs in user with session
        return waiter

    @staticmethod
    def logout_waiter(request):
        """Logs out the waiter by clearing the session."""
        logout(request)