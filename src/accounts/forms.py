from custom_user.models import EmailUser
from django import forms


class EmailUserLoginForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	
