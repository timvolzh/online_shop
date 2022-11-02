from typing import List

from abstracts.utils import send_email


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
