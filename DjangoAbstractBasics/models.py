from django.db import models
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
# Create your models here.


#This User moder defines the AbstractBaseUser model. It should contain basic and general data relevant to all kinds of users
class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	#username = models.CharField(_('Username'), unique=True, max_length=49)
	first_name = models.CharField(_('First Name'), max_length=59)
	last_name = models.CharField(_('Last Name'), max_length=59)
	photo = models.ImageField(_('Profile Photo'), max_length=200, blank=True, null=True, upload_to='photo')
	slug = models.SlugField(help_text='for url purposes')

	#automated fields...non admins can't alter these fields
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	last_login = models.DateTimeField(_('last login'), auto_now=True, null=True)
	is_active = models.BooleanField(_('active'), default=True)
	is_staff = models.BooleanField(_('staff'), default=False)
	
	objects = UserManager()

	USERNAME_FIELD = 'email' #or 'username' 
	REQUIRED_FIELDS = ['first_name', 'last_name', 'slug']

	class Meta:
		verbose_name = _('User')
		verbose_name_plural = _('All Users')

	def __str__(self):
		return self.get_full_name()

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name

	def get_short_name(self): #should return first name of the user
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		#sends an email to this user
		send_mail(subject, message, from_email, [self.email], **kwargs)

# 	def get_absolute_url(self):
#		return reverse('__Name of Url__', kwargs={'slug': self.slug})