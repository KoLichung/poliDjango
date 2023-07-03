
from django.core.mail import send_mail
from django.conf import settings

def send_test_mail(title, message):
    send_mail(
        subject=title,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS])