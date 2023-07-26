from django.db import models
from django.contrib.auth.models import ( BaseUserManager
           , AbstractBaseUser       
 )

class CustomUserManager(BaseUserManager):
    def create_user_model(self, email, password=None, **extra_fileds):
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
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'


    objects = CustomUserManager()

    def has_perms(self, perm, obj=None):
        return True  # Modify this method to handle object-level permissions if needed

    def has_module_perms(self, app_label):
        return True
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    face_book_profile = models.CharField(max_length=150)
    twitter_profile = models.CharField(max_length=150)
    image = models.ImageField(upload_to='profile_images', null=True, blank=True)

    def __str__(self):
        return self.user.email


