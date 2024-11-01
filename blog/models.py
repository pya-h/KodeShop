from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from user.models import User
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=256, blank=False, verbose_name='عنوان')
    is_visible = models.BooleanField(default=True, verbose_name='نمایش دادن در وبلاگ')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='photos/blogs', blank=True, null=True,  verbose_name='تصویر')
    summary = models.TextField(max_length=128, blank=True, null=True, verbose_name='خلاصه و موضوع پست')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد پست")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به روز رسانی پست")

    body = CKEditor5Field('متن پست', config_name='default')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پست بلاگ'
        verbose_name_plural = 'پست بلاگ'

    def url(self):
        return reverse('blog_post', args = [self.id])
