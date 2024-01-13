from typing import Any
from django.core.management.base import BaseCommand, CommandError

from learning_app.models import * 

from datetime import date

class Command(BaseCommand):

    help = "Fill db with test data"

    def handle(self, *args: Any, **options: Any) -> str | None:

        # Create category

        cat1 = Category.objects.create(name='Программирование')
        cat2 = Category.objects.create(name='Дизайн')
        cat3 = Category.objects.create(name='Финансы')
        cat4 = Category.objects.create(name='Управление')

        # Create role

        role1 = Role.objects.create(name='admin')
        role2 = Role.objects.create(name='student')
        role3 = Role.objects.create(name='teacher')

        # Create teachers

        teach1 = User.objects.create(first_name='Иван',
                                     last_name='Иванов',
                                     role=role3)
        
        teach2 = User.objects.create(first_name='Петр',
                                     last_name='Петров',
                                     role=role3)
        
        teach3 = User.objects.create(first_name='Семён',
                                     last_name='Семёнов',
                                     role=role3)
        
        teach4 = User.objects.create(first_name='Анна',
                                     last_name='Аничкина',
                                     role=role3)

        # Create catalog

        # catalog1 = Catalog.objects.create(name='main_catalog')
        # catalog.courses.
        # Catalog.objects.create(course=crs2)
        # Catalog.objects.create(course=crs3)
        # Catalog.objects.create(course=crs4)

        # Create courses

        crs1 = Course.objects.create(name='Программирование на Python',
                                     category=cat1,
                                     start_date=date(2024,1,15),
                                     finish_date=date(2024,6,15))
        
        crs2 = Course.objects.create(name='Введение в графический дизайн',
                                     category=cat2,
                                     start_date=date(2024,1,15),
                                     finish_date=date(2024,6,15))
        
        crs3 = Course.objects.create(name='Управление финансовыми активами',
                                     category=cat3,
                                     start_date=date(2024,1,15),
                                     finish_date=date(2024,6,15))
        
        crs4 = Course.objects.create(name='Управление в IT-проектах',
                                     category=cat4,
                                     start_date=date(2024,1,15),
                                     finish_date=date(2024,6,15))

        # Create lessons

        l1 = Lesson.objects.create(title='Python. Урок 1',
                                   goals='Цели урока 1',
                                   course=crs1,
                                   teacher=teach1)
        
        l2 = Lesson.objects.create(title='Графический дизайн. Урок 1',
                                   goals='Цели урока 1',
                                   course=crs2,
                                   teacher=teach2)
        
        l3 = Lesson.objects.create(title='Фин. управление. Урок 1',
                                   goals='Цели урока 1',
                                   course=crs3,
                                   teacher=teach3)
        
        l4 = Lesson.objects.create(title='IT управление. Урок 1',
                                   goals='Цели урока 1',
                                   course=crs4,
                                   teacher=teach4)
