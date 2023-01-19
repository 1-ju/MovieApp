from django.contrib import admin

from dashboard.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'description', 'nickname', 'image')