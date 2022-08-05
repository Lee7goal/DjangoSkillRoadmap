from django.forms import ModelForm, widgets
from account_manager.models import AccountModel


class LoginForm(ModelForm):
    class Meta:
        model = AccountModel
        fields = ('username', 'password')

        widgets = {
            'username': widgets.Input(attrs={'class': 'form-control'}),
            'password': widgets.Input(attrs={'class': 'form-control', 'type': 'password'}),
        }