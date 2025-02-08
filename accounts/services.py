from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from .models import Waiter



class WaiterService:

    @staticmethod
    def create_waiter(username, password):
        """Creates a new Waiter instance."""
        return Waiter.objects.create(username=username, password=password)

    @staticmethod
    def get_waiter(waiter_id):
        """Retrieves a single Waiter instance."""
        return get_object_or_404(Waiter, id=waiter_id)

    @staticmethod
    def list_waiters():
        """Returns all Waiters."""
        return Waiter.objects.all()

    @staticmethod
    def update_waiter(waiter_id, username=None, password=None):
        """Updates an existing Waiter."""
        waiter = get_object_or_404(Waiter, id=waiter_id)
        if username:
            waiter.username = username
        if password:
            waiter.password = password  # The model's save method will hash the password
        waiter.save()
        return waiter

    @staticmethod
    def delete_waiter(waiter_id):
        """Deletes a Waiter instance."""
        waiter = get_object_or_404(Waiter, id=waiter_id)
        waiter.delete()
        return True

    @staticmethod
    def register_waiter(username, password):
        """Registers a new waiter with a hashed password."""
        if Waiter.objects.filter(username=username).exists():
            raise ValueError("Username already exists")
        return Waiter.objects.create(username=username, password=make_password(password))

    @staticmethod
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