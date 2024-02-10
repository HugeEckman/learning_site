from typing import Any
from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        send_mail(
            "Subject here",
            "Here is the message",
            "123@456.com", # from 
            ['dartv80@mail.ru'] # to
        )

        