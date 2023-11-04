"""configuartion of the admin inyerface for microbloggs"""

from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''config of the admin interface for users'''
    list_display = [
        'username', 'first_name', 'last_name', 'email', 'is_active', 'bio',
    ]
