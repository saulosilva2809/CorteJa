from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@shared_task(bind=True, max_retries=3)
def send_email(self, subject: str, to: str, html_body: str, text_body: str | None = None, from_email: str | None = None):
    try:
        sender = from_email or getattr(settings, 'DEFAULT_FROM_EMAIL',)
        plain = text_body or 'Visualize esta mensagem em formato HTML.'

        msg = EmailMultiAlternatives(
            subject=subject,
            body=plain,
            from_email=sender,
            to=[to],
        )
        msg.attach_alternative(html_body, "text/html")
        msg.send()
        return {"status": "sent", "to": to}

    except Exception as exc:
        raise self.retry(exc=exc, countdown=10)
