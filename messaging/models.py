from django.db import models
from user.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False, related_name='sender_user')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                 default=None, related_name='receiver_user')
    subject = models.CharField(max_length=256, blank=True, null=True, default=None)
    content = models.TextField()

    tag = models.CharField(max_length=64, blank=True, null=True, default=None)   # admin can set this to group
    # filter messaging in admin panel

    def __str__(self):
        return f'{self.sender}: {self.content}'

    @property
    def short(self):
        return self.content[:10]

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
