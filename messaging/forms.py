from django import forms
from .models import Message


class SupportMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'content']

    def __init__(self, *args, **kwargs):
        super(SupportMessageForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(SupportMessageForm, self).clean()
        content: str = cleaned_data.get('content')
        if not content or len(content.strip()) < 3:
            raise forms.ValidationError('محتوای پیام بسیار کوتاه است!')
