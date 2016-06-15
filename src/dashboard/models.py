from django.db import models
from django.conf import settings




class GlobalInfo(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	trial_expired = models.BooleanField(default=False)
	PLANS = (
		('f', 'FREE'),
		('p', 'PAYING')
	)
	plan = models.CharField(max_length=12, choices=PLANS, default='f')




class BasicInfo(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	willgo_name = models.CharField(max_length=32, unique=True)
	company_name = models.CharField(max_length=120, blank=True, null=True)
	company_zip = models.CharField(max_length=13)
	company_address = models.CharField(max_length=120)
	company_address2 = models.CharField(max_length=120)
	email_address = models.EmailField(blank=True, null=True)
	company_tel = models.CharField(max_length=32, blank=True, null=True)
	is_filled = models.BooleanField(default=False)
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.willgo_name
