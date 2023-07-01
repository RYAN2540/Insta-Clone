from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_signup_email(name, receiver):
    # Creating message subject and sender
    subject = 'Instagram account created.'
    sender = 'ryandev254@gmail.com'

    # passing in the context vairables
    text_content = render_to_string('email/signup-email.txt', {"name": name})
    html_content = render_to_string('email/signup-email.html', {"name": name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
