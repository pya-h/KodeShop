from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime


class UserManager(BaseUserManager):
    def validate_credentials(self, phone, password, fname, lname, email):
        if not phone:
            raise ValueError('Phone number field is essential')
        if not password: # and some other properties
            raise ValueError('Password must be stronger')
        if not fname or not lname:
            raise ValueError('Both name fields are essential')

    def create_user(self, phone, password, fname, lname, email):
        self.validate_credentials(phone, password, fname, lname, email)
        new_user = self.model(phone=phone, fname=fname, lname=lname, email=self.normalize_email(email))
        new_user.set_password(password)
        new_user.is_staff = new_user.is_superuser = False
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, phone, password, fname, lname, email):
        self.validate_credentials(phone, password, fname, lname, email)
        owner = self.model(phone=phone, fname=fname, lname=lname, email=self.normalize_email(email))
        owner.set_password(password)
        owner.is_activated = False
        owner.is_staff = owner.is_superuser = True
        owner.save(using=self._db)
        return owner


class User(AbstractBaseUser):
    fname = models.CharField(max_length=30, verbose_name="نام")
    lname = models.CharField(max_length=30, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=11, unique=True, verbose_name="شماره موبایل")
    email = models.CharField(max_length=100, unique=True, verbose_name="ایمیل")
    ip = models.CharField(max_length=20, blank=True, verbose_name="IP")

    joining_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ عضویت")
    last_login = models.DateTimeField(auto_now=True, verbose_name="آخرین ورود")
    is_staff = models.BooleanField(default=False, verbose_name="کاربر کارمند")
    is_superuser = models.BooleanField(default=False, verbose_name="کاربر ادمین")
    is_activated = models.BooleanField(default=False, verbose_name="حساب کاربری فعال")

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['fname', 'lname', 'email']
    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.fname} {self.lname}'

    def ID(self):
        return self.id

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return self.is_superuser

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    avatar = models.ImageField(blank=True, upload_to='photos/avatars/', null=True)
    last_email_date = models.DateTimeField(default=None, blank=True, null=True)
    debt = models.IntegerField(default=0, verbose_name='بدهی شما')
    postal_code = models.CharField(max_length=10, verbose_name="کدپستی", blank=True)
    province = models.CharField(max_length=30, verbose_name="استان", blank=True)
    city = models.CharField(max_length=30, verbose_name="شهرستان", blank=True)
    address = models.TextField(max_length=64, verbose_name="نشانی", blank=True)

    def __str__(self):
        return self.user.__str__()

    @staticmethod
    def get_email_time_passed(u):
        profile = None
        time_passed_from_last_email = -1

        try:
            profile = Profile.objects.get(user=u)
            time_passed_from_last_email = datetime.now().timestamp() - profile.last_email_date.timestamp() \
                if profile.last_email_date else -1
        except Profile.DoesNotExist:
            time_passed_from_last_email = -1
        return time_passed_from_last_email, profile

    def full_address(self):
        return f'{self.province} - {self.city} - {self.address}'

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"
