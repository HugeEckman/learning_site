from django_rq import job
from django.core.mail import send_mail


def send_email_to_user(**properties):
    subject = 'Contacting support'
    message_text = 'Thanks for contacting support\nsend_email_to_user'
    from_email = 'informing@learning_app.co'
    to_email = 'user@learning_app.co'

    send_mail(
        subject=subject,
        message=message_text,
        from_email=from_email,
        recipient_list=[to_email]
    )


def send_email_to_admin(**properties):
    subject = 'Contacting support'
    message_text = 'You have one unread message\nsend_email_to_admin'
    from_email = 'informing@learning_app.co'
    to_email = 'admin@learning_app.co'

    send_mail(
        subject=subject,
        message=message_text,
        from_email=from_email,
        recipient_list=[to_email]
    )