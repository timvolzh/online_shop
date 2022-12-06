from typing import List

from django.conf import settings
from django.core.mail import send_mail
# from apps.abstracts.utils import send_email


from celery import Celery


celery_app = Celery('app',
                    broker='redis://127.0.0.1:6379/5',
                    backend='redis://127.0.0.1:6379/6'
                    )


def send_email(
    subject: str,
    text: str,
    receiver_emails: List[str]
) -> bool:
    """Send email."""
    try:
        send_mail(
            subject=subject,
            message=text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=receiver_emails
        )
        return True
    except Exception as e:
        print("Email error:", e)
        return False

@celery_app.task
def email_changed_order_status(
    order_id: int,
    new_status: str,
    receivers: List[str]
) -> None:
    """Send email with changed status."""
    send_email(
        subject="Изменение статуса заказа",
        text=f"Поздравляем! Статус заказа {order_id} изменился на {new_status}",
        receiver_emails=receivers
    )

