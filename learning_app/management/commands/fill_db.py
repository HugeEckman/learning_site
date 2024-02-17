from typing import Any
from django.core.management.base import BaseCommand

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

        # Create students

        user1 = User.objects.create(first_name='Иван',
                                    last_name='Иванов')
        
        user2 = User.objects.create(first_name='Петр',
                                    last_name='Петров')
        
        user3 = User.objects.create(first_name='Семён',
                                    last_name='Семёнов')
        
        user4 = User.objects.create(first_name='Анна',
                                    last_name='Аничкина')
        
        user5 = User.objects.create(first_name='Света',
                                    last_name='Светикова')
        
        user6 = User.objects.create(first_name='John',
                                    last_name='Doe')
        
        user7 = User.objects.create(first_name='Jane',
                                    last_name='Doe')
        
        user8 = User.objects.create(first_name='Bill',
                                    last_name='Jobs')
        
        user9 = User.objects.create(first_name='Steve',
                                    last_name='Gates')
        
        user10 = User.objects.create(first_name='Steve',
                                    last_name='Vozniak')
        
        # Create teachers

        teach1 = Teacher.objects.create(first_name='Nick',
                                        last_name='Valentine')
        
        teach2 = Teacher.objects.create(first_name='Sew',
                                        last_name='Jo')
        
        teach3 = Teacher.objects.create(first_name='Wade',
                                        last_name='Wilson')
        
        teach4 = Teacher.objects.create(first_name='Steve',
                                        last_name='Star')

        # Create courses

        crs1 = Course.objects.create(name='Программирование на Python',
                                     category=cat1,
                                     start_date=date(2024,1,15),
                                     finish_date=date(2024,6,15),
                                     teacher = teach1)
        
        crs1.students.add(user1, user2, user3)

        crs2 = Course.objects.create(name='Введение в графический дизайн',
                                     category=cat2,
                                     start_date=date(2024,1,15),
                                     finish_date=date(2024,6,15),
                                     teacher = teach2)
        
        crs2.students.add(user2, user4)
        
        crs3 = Course.objects.create(name='Управление финансовыми активами',
                                     category=cat3,
                                     start_date=date(2024,1,15),
                                     finish_date=date(2024,6,15),
                                     teacher = teach3)
        
        crs3.students.add(user4, user5, user3)
        
        crs4 = Course.objects.create(name='Управление в IT-проектах',
                                     category=cat4,
                                     start_date=date(2024,1,15),
                                     finish_date=date(2024,6,15),
                                     teacher = teach2)
        
        crs4.students.add(user6, user7, user8, user9, user10)

        # Create lessons

        l1 = Lesson.objects.create(title='Python. Урок 1',
                                   goals='Цели урока 1',
                                   course=crs1, )
        
        l2 = Lesson.objects.create(title='Графический дизайн. Урок 1',
                                   goals='Цели урока 1',
                                   course=crs2)
        
        l3 = Lesson.objects.create(title='Фин. управление. Урок 1',
                                   goals='Цели урока 1',
                                   course=crs3)
        
        l4 = Lesson.objects.create(title='IT управление. Урок 1',
                                   goals='Цели урока 1',
                                   course=crs4)
        
        l5 = Lesson.objects.create(title='Python. Урок 2',
                                   goals='Цели урока 2',
                                   course=crs1)
        
        l6 = Lesson.objects.create(title='Графический дизайн. Урок 2',
                                   goals='Цели урока 2',
                                   course=crs2)
        
        l7 = Lesson.objects.create(title='Фин. управление. Урок 2',
                                   goals='Цели урока 2',
                                   course=crs3)
        
        l8 = Lesson.objects.create(title='IT управление. Урок 2',
                                   goals='Цели урока 2',
                                   course=crs4)
