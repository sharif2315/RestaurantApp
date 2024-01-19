from django.core.mail import send_mail
from django.conf import settings


def send_notification_email(contact_submission):
    send_mail(
        subject=f"New Contact from {contact_submission.name}",
        message=contact_submission.message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_EMAIL],
    )
