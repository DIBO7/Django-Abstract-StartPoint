from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		#creates and saves a user with a given email and password
		if not email:
			raise ValueError('You must provide us with your valid email address')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		extra_fields.setdefault('is_staff', False)

		if extra_fields.get('is_staff') is not False:
			raise ValueError("user account conflict")
			
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Admin property must be enabled')

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Staff property must be enabled!')

		return self._create_user(email, password, **extra_fields)

	def create_staffuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		extra_fields.setdefault('is_staff', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Staff property must be enabled')

		return self._create_user(email, password, **extra_fields)