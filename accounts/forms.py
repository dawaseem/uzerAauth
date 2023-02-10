from django import forms

class LoginForm(forms.Form):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)