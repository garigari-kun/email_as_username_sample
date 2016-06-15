from django.contrib import admin

from .models import BasicInfo, GlobalInfo

admin.site.register(GlobalInfo)
admin.site.register(BasicInfo)
