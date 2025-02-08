from django.contrib import admin
from .models import Waiter

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
        """Ensure password is hashed when saved from the admin panel."""
        if change and form.cleaned_data.get("password"):
            obj.set_password(form.cleaned_data["password"])
        obj.save()
