from django.urls import path
from .views import (WaiterLoginView, WaiterLogoutView)

urlpatterns = [
    path('login/', WaiterLoginView.as_view(), name='waiter-login'),
    path('logout/', WaiterLogoutView.as_view(), name='waiter-logout'),
]

