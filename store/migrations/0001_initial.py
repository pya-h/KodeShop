# Generated by Django 5.0.7 on 2024-09-17 15:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='نام به انگلیسی')),
                ('name_fa', models.CharField(max_length=64, unique=True, verbose_name='نام')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='اسلاگ')),
                ('description', models.TextField(blank=True, max_length=1024, verbose_name='مشخصات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('stock', models.IntegerField(verbose_name='موجودی')),
                ('available', models.BooleanField(default=True, verbose_name='در دسترس؟')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد این محصول')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرزین تغییر اطلاعات')),
                ('discount', models.IntegerField(default=0, verbose_name='تخفیف')),
                ('image', models.ImageField(upload_to='photos/products', verbose_name='تصویر')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالا ها',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/products', verbose_name='تصویر')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='کالای مرتبط')),
            ],
            options={
                'verbose_name': 'گالری',
                'verbose_name_plural': 'گالری',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=500, verbose_name='نظر')),
                ('rating', models.FloatField(verbose_name='امتیاز')),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد نظر')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='به روز رسانی اطلاعات نظز')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='کالای مرتبط')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر کاربران',
                'verbose_name_plural': 'نظرات کاربران',
            },
        ),
    ]
