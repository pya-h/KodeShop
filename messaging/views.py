from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import SupportMessageForm
from .models import Message
from django.contrib import messages


@require_http_methods(["POST"])
def send_support_message(request):
    if request.user.is_authenticated:
        try:
            form = SupportMessageForm(request.POST)
            if form.is_valid():
                subject: str = form.cleaned_data.get('subject')
                content: str = form.cleaned_data.get('content')
                new_msg = Message(sender_id=request.user.id, subject=subject.strip() if subject else None,
                                  content=content.strip())
                new_msg.save()
                messages.success(request, 'پیام شما برای ما ارسال شد.')
        except Exception as x:
            print(x)
            messages.error(request, 'متاسفانه ارسال پیام شما با خطا مواجه شد. لطفا لحظاتی بعد مجددا تلاش کنید.')
    else:
        messages.error(request, 'برای ارسال نظر ابتدا باید وارد حساب کاربری خود شوید.')
    return redirect(request.META.get('HTTP_REFERER'))


@require_http_methods(["GET"])
def contact_us(request):
    return render(request, 'us/contact.html', {'form': SupportMessageForm()})
