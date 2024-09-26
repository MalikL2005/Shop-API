from .models import User 
from django.forms import ModelForm

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        required = ['username', 'first_name', 'last_name', 'email', 'password']