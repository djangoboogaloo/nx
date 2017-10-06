from django.contrib import admin

# Register your models here.
from .models import Profile

class user_view(admin.ModelAdmin):
	list_display = ["user","balance","email_confirmed"]
	class Meta:
		model = Profile


admin.site.register(Profile, user_view)