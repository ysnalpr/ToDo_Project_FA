from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	

from .models import User

# Register your models here.

admin.site.register(User, UserAdmin)

UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', 'date_of_birth', 'image')


