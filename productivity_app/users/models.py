from django.db import models
from django.contrib.auth.models import ( BaseUserManager
           , AbstractBaseUser       
 )

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
class User (AbstractBaseUser):
    email = models.EmailField(
        verbose_name= 'email address',
        max_length= 225,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

