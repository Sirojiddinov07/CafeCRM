from django.contrib.auth.base_user import BaseUserManager


class WaiterManager(BaseUserManager):
    """Custom manager for Waiter model."""

    def create_waiter(self, username, password=None):
        if not username:
            raise ValueError("Waiters must have a username")
        waiter = self.model(username=username)
        if password:
            waiter.set_password(password)
        waiter.save(using=self._db)
        return waiter