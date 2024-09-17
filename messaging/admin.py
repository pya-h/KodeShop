from django.contrib import admin
from .models import Message


class MessageAdminPanel(admin.ModelAdmin):
    list_display = ('sender', 'subject', 'short', 'tag')
    list_filter = ('sender', 'receiver', 'tag', 'subject')
    search_fields = (
        'tag', 'content', 'subject', 'sender__fname', 'sender__lname', 'receiver__fname', 'receiver__lname',
    )
    readonly_fields = ('sender', 'receiver', 'content', 'subject')
    list_per_page = 20


admin.site.register(Message, MessageAdminPanel)