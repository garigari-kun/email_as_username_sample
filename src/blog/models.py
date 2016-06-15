from django.conf import settings
from django.db import models

class Blog(models.Model):
	admin_staff = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=120)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title
