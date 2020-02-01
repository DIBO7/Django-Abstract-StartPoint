from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('Email is already taken and in use')
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Password does not match')
		return password2

	def save(self, commit=True):
		#saves provided password in hashed format
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password2"])
		if commit:
			user.save()
		return user


class UserAdminCreationForm(forms.ModelForm):
	#for creating new users, includes all fields plus a repeated password
	password1 = forms.CharField(label='Input Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'slug')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('Email is already taken and in use')
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Password does not match')
		return password2

	def save(self, commit=True):
		#saves provided password in hashed format
		user = super(UserAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserAdminChangeForm(forms.ModelForm):
	#to update users, includes all the fields but replaces password with password hash display field
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ('email', 'password', 'is_active', 'is_staff')

	def clean_password(self):
		#regardless of what the user provides, return the initial value
		#this is done here, rather than on the field, because the 
		#field does not have access to the initial value
		return self.initial['password']