# Generated by Django 5.0.7 on 2024-08-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربر ها'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, max_length=64, verbose_name='نشانی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=30, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_activated',
            field=models.BooleanField(default=False, verbose_name='حساب کاربری فعال'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='کاربر کارمند'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='کاربر ادمین'),
        ),
        migrations.AlterField(
            model_name='user',
            name='joining_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='آخرین ورود'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(max_length=30, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل'),
        ),
    ]
