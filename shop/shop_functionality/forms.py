from .models import User 
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        required = ['username', 'first_name', 'last_name', 'email', 'password']