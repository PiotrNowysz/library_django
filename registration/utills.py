from django.core.mail import EmailMessage


def send_mail_to(title, user_mail, content):
    message = EmailMessage(
        title,
        content,
        'mailneuna@gmail.com',
        [user_mail],
    )
    message.send()
