'''
Admin Group is currently enabled in the admin.
To disable it, uncomment the codes below
'''
#from django.contrib.auth.models import Group
#admin.site.unregister(Group)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import *
# Register your models here.

class UserAdmin(BaseUserAdmin):
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm

	list_display = ('first_name', 'last_name', 'date_joined', 'last_login')
	list_filter = ('is_staff', 'date_joined', 'last_login')
	fieldsets = (
		('Account/Contact', {'fields': ('email', 'password')}),
		('Personal Info', {'fields': ('photo', 'first_name', 'last_name', 'slug')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
		)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'first_name', 'last_name', 'slug', 'password1', 'password2')}
			),
		)
	search_fields = ('email', 'first_name', 'last_name')
	ordering = ('email', 'date_joined', 'first_name', 'last_name')
	filter_horizontal = ()

admin.site.register(User, UserAdmin)