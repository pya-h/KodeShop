from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from user.models import User
from django.urls import reverse
from enum import Enum


class PostBase(models.Model):
    title = models.CharField(max_length=256, blank=False, verbose_name='عنوان')
    is_visible = models.BooleanField(default=True, verbose_name='نمایش دادن')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='مالک')
    summary = models.TextField(max_length=128, blank=True, null=True, verbose_name='خلاصه و موضوع پست')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به روز رسانی")

    def __str__(self):
        return self.title

    def url(self):
        pass


class BlogPost(PostBase):
    thumbnail = models.ImageField(upload_to='posts/blogs', blank=True, null=True, verbose_name='تصویر')
    body = CKEditor5Field('متن پست', config_name='default')

    class Meta:
        verbose_name = 'پست بلاگ'
        verbose_name_plural = 'پست بلاگ'

    def url(self):
        return reverse('blog_post', args=[self.id])


class VideoQualityEnum(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class VideoPost(PostBase):
    thumbnail = models.ImageField(upload_to='posts/videos/thumbnails', blank=True, null=True,
                                  verbose_name='تصویر پیش نمایش')
    caption = models.TextField(blank=True, null=True, verbose_name='کپشن ویدیو')
    original_video = models.FileField(upload_to='videos/', verbose_name='فایل ویدیو (کیفیت اصلی) *')
    low_quality_video = models.FileField(upload_to='videos/low/', blank=True, null=True,
                                         verbose_name='نسخه کیفیت پایین ویدیو (اختیاری)')
    medium_quality_video = models.FileField(upload_to='videos/medium/', blank=True, null=True,
                                            verbose_name='نسخه کیفیت متوسط ویدیو (اختیاری)')

    class Meta:
        verbose_name = 'ویدیو بلاگ'
        verbose_name_plural = 'ویدیو بلاگ'

    def url(self):
        return reverse('video_post', args=[self.id])

    def get(self, quality: int = 2):
        match quality:
            case VideoQualityEnum.LOW.value:
                return self.low_quality_video.url
            case VideoQualityEnum.MEDIUM.value:
                return self.medium_quality_video.url
            case _:
                return self.original_video.url
