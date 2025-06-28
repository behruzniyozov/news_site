from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_user_register_email(email, token):
    subject = "Confirm your email address"
    to_email = email
    context = {
        "token": token,
        "frontend_url": "news_site.com",
    }
    html_content = render_to_string("user_register_email.html", context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = "html"
    email.send()