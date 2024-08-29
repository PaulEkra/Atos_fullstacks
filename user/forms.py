from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # instance = kwargs.get('instance')
        # if instance is not None:
        #     self.fields['pseudo'].widget.attrs.update({
        #         'hidden': True,
        #         'label': ''
        #     })
        self.fields['username'].help_text = ''

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'},),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
