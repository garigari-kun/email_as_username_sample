from django import forms
from .models import BasicInfo

class BasicInfoForm(forms.ModelForm):


	class Meta:
		model = BasicInfo
		fields = [
			'willgo_name',
			'company_name',
			'email_address',
			'company_tel',
		]
