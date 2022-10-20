from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


# Create your models here.


class SiteUserManager(BaseUserManager):
    '''Custom UserManager'''
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class SiteUser(AbstractBaseUser):
    '''Custom User'''
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=40)
    username = models.CharField(verbose_name='Псевдоним', max_length=20, unique=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    register_date = models.DateField(verbose_name='Дата регистрации', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(verbose_name='Профиль активен', default=True)

    objects = SiteUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
