from typing import Any
from django.core.management.base import BaseCommand, CommandError

from learning_app.models import * 

class Command(BaseCommand):

    help = "Remove data from all tables"

    def handle(self, *args: Any, **options: Any) -> str | None:
        Category.objects.all().delete()
        Course.objects.all().delete()
        Teacher.objects.all().delete()
        # Catalog.objects.all().delete()
        Lesson.objects.all().delete()

