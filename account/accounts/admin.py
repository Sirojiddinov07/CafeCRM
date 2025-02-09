from django.contrib import admin
from django.contrib.auth.hashers import make_password
from account.accounts.models import Waiter

@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    """Admin panel for managing waiters."""

    list_display = ('id', 'username')
    search_fields = ('username',)
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )

    def save_model(self, request, obj, form, change):
        """Ensure the password is always hashed when saving."""
        if form.cleaned_data.get("password"):
            obj.password = make_password(form.cleaned_data["password"])
            super().save_model(request, obj, form, change)
