from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account_manager.views import AccountLoginView

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]