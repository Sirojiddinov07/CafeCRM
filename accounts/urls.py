from django.urls import path
from .views import (WaiterListCreateView, WaiterDetailView, WaiterRegisterView,
                    WaiterLoginView, WaiterLogoutView)

urlpatterns = [
    path('waiters/', WaiterListCreateView.as_view(), name='waiter-list'),
    path('waiters/<int:waiter_id>/', WaiterDetailView.as_view(), name='waiter-detail'),
    path('register/', WaiterRegisterView.as_view(), name='waiter-register'),
    path('login/', WaiterLoginView.as_view(), name='waiter-login'),
    path('logout/', WaiterLogoutView.as_view(), name='waiter-logout'),
]

