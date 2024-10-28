from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from user.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=256, blank=False, verbose_name='عنوان')
    body = RichTextUploadingField(verbose_name='متن پست')
    is_visible = models.BooleanField(default=True, verbose_name='نمایش دادن در وبلاگ')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد پست")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به روز رسانی پست")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پست بلاگ'
        verbose_name_plural = 'پست بلاگ'

