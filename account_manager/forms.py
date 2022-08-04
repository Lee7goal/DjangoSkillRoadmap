from django.forms import ModelForm

from account_manager.models import AccountModel


class LoginForm(ModelForm):
    class Meta:
        model = AccountModel
        fields = ('username', 'password')
